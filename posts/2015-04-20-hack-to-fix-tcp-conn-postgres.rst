.. title: How to Fix What You Can't Kill: Undead PostgreSQL queries.
.. slug: hack-to-terminate-tcp-conn-postgres
.. date: 2015/04/20 17:30:42
.. tags: shell network postgresql postgres howto hack tcp connection keepalive
.. link:
.. description: How to Fix What You Can’t Kill: IDLE PostgreSQL connection with TCP ESTABLISHED state with clients that are already gone.
.. author: Sandor Szuecs
.. type: text
.. image: binary.png


The standard way to kill a TCP connection in ``PostgreSQL`` is to use ``pg_terminate_backend($PID)``. However, in some situations this function does not work. To help you avoid negative outcomes when closing such connections, here is a simple hack.


.. TEASER_END


Undead queries
==============


The Zalando team relies on PostgreSQL for almost all backend applications and we manage more than a hundred database clusters reliably storing terabytes of data.


Recently we noticed that a few of our queries were running for hours or even days without terminating. Because our team sets most of our databases to terminate queries after 10 minutes (with ``statement_timeout`` set to ``'10m'``), this outcome was completely unexpected.


We started to investigate and discovered that:

* in most cases, these never-ending queries were returning a lot of data (sometimes even megabytes);
* recipients of the data were non-existent;
* query was not killable by ``select pg_terminate_backend($PID)`` call;
* process of that query was waiting for ``send()`` syscall to finish;
* the underlying TCP connection was in the TCP ESTABLISHED state, but the client was already gone, so no data was being transmitted over it. Postgres tracks this connection as IDLE.


===========
The problem
===========


Such an undead query introduced at least two major issues:

* it is impossible to shutdown the cluster nicely (as postgres will be waiting for query termination or will try to send software termination signal (``TERM``) to all running queries and will still wait until they terminate, so the only way to stop the cluster with undead query would be to use ``--immediate`` option or effectively sending non-ignorable ``KILL`` signal to all the processes and crashing the server.
* long running transactions (and such an undead query is a transaction from the point of view of PostgreSQL) stop the advancing of the event horizon (or the transaction ID of the oldest running query) and this in turn does not allow ``(AUTO)VACUUM`` to clean up any records, that have been modified after the beginning of the oldest running query.


==================
What is happening?
==================


It looks like the undead queries are the result of situations, when ``send()`` system call waits for the data to be transferred over the TCP connection, but the recipient does not receive it. There are several possibilities here:

* client host died with power failure or there was a network issue and the TCP connection on the server host did not realise it. In this case the TCP keepalive mechanism will kick in and try to detect, that the connection is dead (see http://tldp.org/HOWTO/TCP-Keepalive-HOWTO/usingkeepalive.html);
* client application is hanging (or paused) and does not receive any data from the server, in this case keepalive works fine and the ``send()`` syscall will never end, even when a ``TERM`` signal was sent to it, because PostgreSQL is using ``SA_RESTART`` flag for signal processing and ``SO_SNDTIMEO`` is not used at all (see ``man 7 signal``).


===========
What to do?
===========


Probably first of all one should reduce the keepalive detection timeout to some more reasonable time (default is 2 hours + 9 * 75 sec or about 2 hours and 12 minutes). One can do that by changing the default system settings or by tuning postgres configuration parameters (see http://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-TCP-KEEPALIVES-IDLE)


But when you already have an undead query running and you are sure that the client does not exist the solution can be to forcefully close the TCP connection.


To do that you can either

- send a TCP packet with a ``FIN`` flag
- send a TCP packet with an ``RST`` flag


As we do not expect, that the the client will answer the ``FIN`` flag, sending ``RST`` flag will do the nasty job of closing our ``ESTABLISHED`` TCP connection without waiting for a response from the client.


===========================
How to Send an ``RST`` Flag
===========================


To send a correct ``RST`` packet, collect all the information you need
to break into a TCP stream:

- SRC IP
- SRC TCP port
- DST IP -> DB-Host
- DST TCP port -> 5432
- Sequence number


Because we have full control of our database host, as well as the PID of the process that holds the connection (in this case, ``34140``), we can easily collect all unknown information:


.. code:: bash

        $ # DB-Host
        $ ps fauxww | grep 34140
        postgres 34140  0.5  0.0 13042260 9040 ?           Ss   Apr01   5:13  \_ postgres: robot prod_eventlog_db 10.161.137.203(50166) SELECT


As you can see, the SRC IP is `10.161.137.203` and the SRC ``TCP`` port is
`50166`.


Now we have to get the current sequence number to attack the target ``TCP`` stream. You might have to wait a while to see a packet -- this will depend on the keepalive settings (if the default values are used, then not longer than 2 hours):


.. code:: bash

        # DB-Host
        $ tcpdump -vvni any host 10.161.137.203 and port 50166
        10:08:02.679268 IP (tos 0x0, ttl 123, id 10348, offset 0, flags [DF], proto TCP (6), length 41)
        10.161.137.203.50166 > 10.10.116.76.5432: Flags [.], cksum 0xcaaa (correct), seq 130742508:130742509, ack 2921339488, win 0, length 1


Our sequence number is `130742508`, which we’ll now use to send a spoofed ``TCP`` packet and stop the stream. ``hping3`` can send arbitrary packets via RAW sockets and also helps us to stop the stream:


.. code:: bash

        $ hping3 -a 10.161.137.203 -s 50166 -p 5432 --rst -M 130742508  10.10.116.76


As you can see, in the open ``tcpdump`` session the packet was successfully received:


.. code:: bash

        # running tcpdump on DB-Host
        10:25:41.225359 IP (tos 0x0, ttl 64, id 24896, offset 0, flags [none], proto TCP (6), length 40)
        10.161.137.203.50166 > 10.10.116.76.5432: Flags [R], cksum 0x41f5 (correct), seq 130742508, win 512, length 0


``Postgres`` then closes the process; we send a TCP reset packet signalling that the client does not know about this connection.


We hope this post helps you to fix edge cases with connections to ``postgres`` and avoid frustration along the way. Tell us if it works for you by pinging us on Twitter at @ZalandoTech.


.. _TCP: http://en.wikipedia.org/wiki/Transmission_Control_Protocol
.. _Postgres: http://www.postgresql.org/
.. _tcpdump: http://www.tcpdump.org/tcpdump_man.html
.. _hping3: http://www.hping.org/hping3.html
