.. title: Hack to fix idle TCP connections in Postgres.
.. slug: hack-to-fix-tcp-conn-postgres
.. date: 2015/04/02 11:23:42
.. tags: techmonkeys shell network postgres hack
.. link:
.. description: fix idle TCP connections in Postgres
.. author: Sandor Szücs
.. type: text
.. image: FIXME

Break into TCP connections to terminate IDLE connections in ``Postgres``,
which can not be closed via `pg_terminate_backend()`.

.. TEASER_END

Motivation
==========

From time to time there are IDLE connections in ``Postgres``, which can
be normally killed with `pg_terminate_backend($PID)`. In very seldom
situations these can not be killed, but we have somehow kill them to
get free connections, free allocated memory and if the connection
opened a transaction this could lead to a data write fuckup.

Closing IDLE connections
========================

In order to close an IDLE connection, we have to have an idea what
options do we have to kill them:

- pg> SELECT pg_terminate_backend($PID)
- % kill $PID
- shutdown database
- break into ``TCP`` session to send ``TCP`` `RST` to the IDLE connection

Suppose `pg_terminate_backend()` did not work, we could send a `SIGTERM`
to the pid of the sleeping Query with `kill $PID`, which could lead to
unexpected behavior. We also could switch the Master to a Slave and
restart the Database, but this will loose some connections. Both seems
to be a way too risky for just terminating ONE idle connection.

There are two ways to close a terminate ``TCP`` connection, sending a ``TCP``
packet with a FIN flag or sending a `RST` flag. The last one is the way
I choose, because `RST` will just close the connection and does not need
an answer.

In order to send a correct `RST` packet we have to get all information
we need to break into a ``TCP`` stream:
- SRC IP
- SRC ``TCP`` port
- DST IP -> DB-Host
- DST ``TCP`` port -> 5432
- Sequence number

Since we have full control on our DB host we can easily get all unknown
information. We already have the PID (34140) of the process which hold the connection.

.. code-block:: bash
    # DB-Host
    TPID=34140
    ps uaxfww | grep $TPID
    postgres 34140  0.5  0.0 13042260 9040 ?       Ss   Apr01   5:13  \_ postgres: robot_erp_reader prod_eventlog_db 10.161.137.203(50166) SELECT

As you can see the SRC IP is `10.161.137.203` and the SRC ``TCP`` port is
`50166`. Now we have to get the current sequence number to attack the target
``TCP`` stream.

.. code-block:: bash
    # DB-Host
    tcpdump -vvni any host 10.161.137.203 and port 50166
    10:08:02.679268 IP (tos 0x0, ttl 123, id 10348, offset 0, flags [DF], proto TCP (6), length 41)
    10.161.137.203.50166 > 10.10.116.76.5432: Flags [.], cksum 0xcaaa (correct), seq 130742508:130742509, ack 2921339488, win 0, length 1

We got 130742508 as sequence number and will use it to send a spoofed
``TCP`` packet to stop the stream using ``hping3``. ``hping3`` is able to send
arbitrary packets via RAW sockets.

.. code-block:: bash
    hping3 -a 10.161.137.203 -s 50166 -p 5432 --rst -M 130742508  10.10.116.76

As you can see in the open ``tcpdump`` session the packet was successfully received.
.. code-block:: bash
    # running tcpdump on DB-Host
    10:25:41.225359 IP (tos 0x0, ttl 64, id 24896, offset 0, flags [none], proto TCP (6), length 40)
    10.161.137.203.50166 > 10.10.116.76.5432: Flags [R], cksum 0x41f5 (correct), seq 130742508, win 512, length 0

The process was closed by ``Postgres``. done.

.. _TCP: http://sen.wikipedia.org/wiki/Transmission_Control_Protocol
.. _Postgres: http://www.postgresql.org/
.. _tcpdump: http://www.tcpdump.org/tcpdump_man.html
.. _hping3: http://www.hping.org/hping3.html
