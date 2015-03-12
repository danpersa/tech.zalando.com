.. title: Camunda Meets Cassandra at Zalando
.. slug: camunda-meets-cassandra-at-zalando
.. date: 2015/03/12 08:00:00
.. tags: cassandra
.. link:
.. description:
.. author: Holger Schmeisky
.. type: text
.. image: dojo_tdd_cycle.jpg

This is a guest post by Daniel Meyer, Technical Lead at Camunda. You can follow him on Twitter here.

Jörn Horstman, André Hartmann and Lukas Niemeier from Zalando’s engineering team visited Camunda earlier this week to present their prototype for running the Camunda engine on Apache Cassandra. If you’re in a hurry, go here to review their slides, and visit the Zalando GitHub page to review their source code.

Zalando is Europe’s leading online fashion platform, with more than 7,000 employees and revenue of €2.2 billion in 2014. They are also Camunda enterprise edition subscribers and use the Camunda process engine for processing orders. Whenever you buy something at Zalando’s online shop, you’re also kicking off a process instance in the Camunda process engine.

Zalando's Current Architecture
==============================

Zalando's system needs to scale horizontally. Zalando's order processing currently runs on PostgreSQL. The tech team partitions their order and process engine data over eight shards, each of which is an independent instance of PostgreSQL. Such an "instance" is a small cluster with replication for performance and failover.

At the application server level, Zalando runs on Apache Tomcat and uses the Spring Framework. For each shard (database), an instance of the Camunda process engine is created. The application is replicated over 16 nodes. When a new order comes in, the application decides in which shard the order data and the corresponding process instance data will be stored. The mapping (orderId -> shard) is stored in a global mapping table. Then the corresponding process instance is started in that shard.


The order processing workflow waits for messages (Payment success, Order cancelled, etc.). Such messages can be sent to any of the nodes, and they must contain an orderId. The application extracts the orderId and, using the mapping table, determines the shard in which the order and the corresponding process instance are stored. Once the shard is determined, the corresponding process engine instance can be resolved and the message is delivered to the process instance waiting for it.

The Zalando team says that this works quite well but presents a few drawbacks:
Engineers need to implement the sharding themselves, including the mapping table. It would be nicer if the sharding of the data was transparent to the application,
You must do queries in monitoring applications against all of the shards and aggregate the data manually
During Zalando’s "Hack Week," Jörn, André and Lukas experimented with Apache Cassandra to explore alternatives to how their current architecture works.

The Cassandra Prototype
=======================
Over the course of a week, the three engineers built a prototype that exchanges the relational DB persistence layer in Camunda with an alternative implementation based on Cassandra. The goal wasn’t to run this in production (yet), but to:
Learn more about Cassandra
Gain a better understanding of the Camunda DB structure

The Zalando prototype provides an alternative implementation of Camunda's PersistenceSession interface. It replicates Camunda's relational model in Cassandra--creating a table for executions in which each execution became a row, as well as tables for variables, tasks, etc. The Zalando team set things up this way on purpose because they wanted to start with a naive implementation and then learn from that.

During the development phase, they multiplexed the persistence session and executed all statements on both a SQL database and Cassandra. This enabled them to enhance support progressively while always having a working system. The result: Successful execution of simple processes.
Lessons Learned
In their presentation, the Zalando team focused on the core process execution use case--steering away from complex monitoring or task queries, which can be implemented on top of a dedicated search database such as Elasticsearch. The latter use case involves feeding data from the execution cluster in near real-time. Near real-time, they said, would be enough for use cases like monitoring or human task management.

Improving the Data Model
Replicating the relational data model is problematic. A single process instance is composed of many entities. Multiple activities can be active inside a process instance at the same time. This results in a “tree” of active activities. Other data objects such as variables, task data or event subscriptions are related to the tree. If a complex data structure is stored as multiple rows in different tables:
Data related to a single process instance is distributed across the cluster. This does not match the process engine's access pattern. Often all or a large portion of the data related to a process instance must be read or updated. If this data is distributed, the network overhead is considerable because data related to a single process instance needs to be collected from many different machines in the cluster.
It isn’t possible to make changes to multiple rows in different tables in an atomic way. However, the process engine often needs to change multiple data objects inside a single process instance.
The Zalandos concluded that it would be better if all data related to a single process instance was stored as a single row inside a single table. Read operations could request it in a single request, and write operations could update it atomically.
Dealing with Eventual Consistency
In their prototype, the Zalandos ignored the the fact that Cassandra employs an eventual consistency model. What does that mean? Well, Cassandra keeps multiple copies of a data item. This allows it to tolerate machine failure and still remain available. When performing a write operation, it is possible to configure whether the operation has to wait for all copies of a particular data item to be updated; whether just one copy is enough; or whether you need something in between, like a quorum. If a data object has been updated on one machine but the update has not been propagated yet to all copies, problems result. If the process engine reads such stale data, the same steps in a process could be executed multiple times, or workflow constructs requiring mutual exclusion or synchronization could malfunction.
It is not clear yet how to overcome these issues, but the Zalando team discussed a lock-based solution:
Assuming that data of a single process instance remains in one row (see above).
If the process engine does work in a process instance, it must first lock the corresponding row. Conceptually, this could be a logical lock based on a retry mechanism.
If the row is updated or deleted, the operation must be performed on all updates and finally release the lock.
The implications of this solution would be:
No intra-process instance concurrency (concurrency inside a single process instance) involving different process engine instances (a single process engine can still lock the row, do things in multiple threads, join the operations and do one atomic update, releasing the lock).
The approach would not tolerate machine failure.

Discussing all of this was a lot of fun! We hope you join us at our future meetups.
