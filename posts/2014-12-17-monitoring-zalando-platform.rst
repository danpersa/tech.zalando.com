.. title: Monitoring the Zalando platform
.. slug: monitoring-the-zalando-platform
.. date: 2014-12-16 12:30:02
.. tags: development,open-source,monitoring,zmon,python,cassandra,redis
.. author: Jan Mussler
.. image: zmon2.png

Some time ago we already presented `our PostgreSQL database monitoring tool`_, but today it's time to unveil how we monitor the other parts of the ZEOS platform. During the past months ZMON was developed to enable almost everyone at Zalando to monitor relevant services and define his or her own alerting on top of it.

.. TEASER_END

Earlier the platform was checked using Icinga/Nagios and a custom frontend, the now old ZMon. However, that setup did not scale with the growing number of services and more importantly with the number of people and teams that had their own requirements and wishes for implementing their checks. Thus two key requirements were taken into account: The new ZMON should scale better in terms of performance and its ability to monitor more entities and equally important: it should enable teams to manage checks and alerts on their own.


Introducing ZMON
================

How does it look like today: ZMON consists of three major components, a Java “Controller” mostly serving the UI using AngularJS, a Python scheduler and a Python worker. Work distribution from scheduler to worker happens via Redis queues, but more on that later. We do use PostgreSQL for storing alerts and imported check definitions, but most of the monitoring state is currently reflected in Redis. Currently we are also evaluating writing the state into Cassandra. Time series data for all metrics is persisted using KairosDB on top of Cassandra.

 .. image:: /images/zmon/zmon-1.png

By design the worker executes a check command targeting a given entity, where an entity is among others a host, a database, or any deployed service. A check yields a result that is in the next step passed on to a set of alert conditions, if the alert evaluates to true, the alert itself raised. Both check command and alert condition are Python expressions, providing a powerful toolset to everyone. Every check is defined in a git repository, we are scanning known project repositories for a folder “zmon-checks” containing yaml definitions of checks. Doing so allows everyone to take care of and manage his own set of checks independently, without any further help, idealy. Any check can have multiple alerts that are defined using the UI and these are assigned a responsible team, commonly the team owning the project or the Incident Management team. Alerts can be cloned or inherited, making it easy to have e.g. different thresholds for different teams or change behavior by time of day. Additionally there are (scheduled) downtimes, SMS and E-Mail notification available.

 .. image:: /images/zmon/zmon-2.png

The schedulers and any number of workers communicate using Redis lists, the scheduler creates a JSON task, containing a check command, a target entity, and the applicable set of alerts. This is passed to the worker, which itself consists of lots of Python processes polling the queue for new tasks. Having received a new task, the command is executed, the alerts evaluated and if necessary the alert state is changed and notifications are sent out. Using the Redis queue allows us to scale the number of workers to support the growing number of checks teams put into place. Python was initially chosen, as it not only provides a well working “eval” function, but also integrates well with lots of system libraries, e.g. snmp or nrpe, and all available database systems. Most checks however do query application specific JSON endpoints or fire SQL queries against our PostgreSQL EventLog database.

 .. image:: /images/zmon/zmon-4.png

Problems..
==========

There were some problems along the way: We first used Celery as a task broker with Redis, however we did not manage to make it run fast enough, and in the end we did not really need a big framework if all we wanted was to encode some task in JSON and fire and forget it into the queue. So Celery was dropped, significantly improving the throughput. This period, marked by problems, has created bad memories, that one really should avoid if when trying to sell a new monitoring solution that people put their trust into. Second, the scheduler is in Python, too, and with the growing number of checks and entities, our implementation for scheduling combined with some cleanup tasks and background threads for refreshing data, was no longer fast enough for issuing checks with intervals < 5s consistently. This was solved with spawning another scheduler responsible only for checks with intervals 30s or less, yielding a much better throughput for low interval checks.

Currently we are adding more features and working on solving/improving one big remaining issue, that is the single point of failure of Redis. We run frontend nodes in all DCs with multiple LBs, for improved availability, similarly also workers run across the DCs and on multiple nodes, but the queue and state is currently a hot topic. On a prototype basis we wrapped all Redis calls, and now mirror writes to our Cassandra cluster. For writing this seems to work well so far, we have a very limited dataset (scales with hosts, applications, checks) and get replication across nodes and DC for free. The results of this migration will remain open for now, but especially the first frontend implementation is much slower, as one comes from very fast Redis, that supports pipeline commands, significantly reducing latency for fetch lots of alert states with a single call.

But for now ZMon is running stable, and recent additions include a REST api to further increase the teams flexibility to manage alerts or poll their own alert state.

Open Source?
============

We believe that with our spliting in checks and alerts using Python expressions and support for teams and responsible teams within the alerting, ZMON currently provides an interesting and very flexibly solution to build your monitoring. That is why during the ongoing Hack-Week one team is working on getting rid of most of the Zalando dependencies and then releasing ZMON as a runnable Vagrant image to play around with. Stay tuned!

Discuss on HackerNews: https://news.ycombinator.com/item?id=8762562

.. _our PostgreSQL database monitoring tool: http://tech.zalando.com/posts/monitoring-postgresql-with-pgobserver.html

