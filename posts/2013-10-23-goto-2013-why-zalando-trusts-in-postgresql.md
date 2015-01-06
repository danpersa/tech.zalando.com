<!--
.. title: GOTO 2013: Why Zalando trusts in PostgreSQL
.. slug: goto-2013-why-zalando-trusts-in-postgresql
.. date: 2013-10-23 11:57:16
.. tags: conference,database,event,postgresql,conference
.. author: Henning Jacobs
.. image: postgresql-db_teaser.png
-->

The [GOTO conference](http://gotocon.com/berlin-2013/) took place in Berlin for the
first time - and Zalando Technology was part of it! Six Zalando developers
attended the conference and we did a presentation on "Why Zalando trusts in
PostgreSQL".

All of us were really happy joining the conference and we learned
a lot. For every talk I heard there was another with opposing opinions — I
think it's good to hear a broad range of opinions and the GOTO conference
facilitated this. I hope to join next year's GOTO Berlin again!

<!-- TEASER_END -->

## Learnings

Some discussion points we took away from the conference:

* **Ever decreasing circles** — what I got out of the discussions on “agile” was that faster feedback cycles are nearly always good: 
    * Get bad news early — doing highest business value first is not always the best idea
    * Short release cycles are better than long ones
    * Pair programming is better than separate code reviews
    * Optimize your test setup to get the most valuable feedback first
* **Balance test effort and time to repair** — Who has to test more? The team needing 30 days to fix a bug in production or the team fixing it on the same day?
* **Large-scale Java deployments are possible within 3 minutes** — If your business model allows downtimes and customer facing errors, you can deploy really fast by restarting all servers at the same time ;-) This is how a big browser game provider does it. Obviously that’s not a solution for us.
* **Care about your interfaces** (new MongoDB driver example) — using explicit parameters with a fluid design like `collection.find(query).withWriteConcern(JOURNALED).updateOne(newValues)` is better than `collection.update(query, newValues, false, false, JOURNALED)`
* **PostgreSQL is expanding to become the NoSQL choice of SQL databases** — that's what Thoughtwork's Technology Radar says and it fits perfectly to our talk...

## Why Zalando trusts in PostgreSQL
NoSQL is on the rise but sadly when people compare the usual NoSQL candidates (Redis, MongoDB, Riak,
Cassandra, HBase, ..) to relational databases they often only mention MySQL.
In our presentation we tried to explain the power of the world’s most advanced
opensource database - PostgreSQL.

[![Zalando's session at GOTO Berlin 2013](/files/2013/10/20131018_102307.jpg)](/files/2013/10/20131018_102307.jpg)
In our session we showed various examples of
why we at Zalando trust PostgreSQL to reliably handle all our data. We make
use of it in various scenarios, from less complex CRUD applications on a
single node, to highly critical and more complex scenarios. This involves
customer and order data with strong constraints for high performance and
availability, sharded across multiple nodes. We believe that PostgreSQL is
massively underrated and that you should have very good reasons to ignore its
great features.

You can download the complete slides from our talk as PDF:

* [Why Zalando trusts in PostgreSQL (GOTO 2013 slides as PDF)](/files/2013/10/GOTO-2013-Why-Zalando-trusts-in-PostgreSQL-20131018.pdf)

