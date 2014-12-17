.. title: Monitoring the Zalando platform
.. slug: monitoring-the-zalando-platform
.. date: 2014-12-16 12:30:02
.. tags: development,open-source,monitoring,zmon,python,cassandra,redis
.. author: Jan Mussler
.. image: zmon2.png

Some time ago we already presented `our PostgreSQL database monitoring tool`_, but today it is time to show you how we monitor the other parts of the Zalando platform. For that particular purpose during the past months ZMON was developed to enable basically everyone at Zalando to monitor relevant services and define his own alerting.

.. TEASER_END

Earlier the platform was checked using Icinga/Nagios and a custom frontend ZMon. However, that setup did not scale with the growing number of services and more important with the number of people and teams that had their own requirements and wishes on implementing their checks. Thus two key requirements were taken into account: ZMON should scale better in terms of performance and ability to monitor more and equally important it should enable teams to manage checks and alerts on their own.


**Introducing ZMON**

How does it look like today in short: ZMON consists of three components, a Java “Controller” mostly serving the UI in AngularJS, a Python scheduler and a Python worker. Work distribution from scheduler to worker happens via Redis, but more on that later. We do use PostgreSQL for storing alert and imported check definitions, but most of the state is currently reflected in Redis. Currently we are also writing the state into Cassandra though, and time series data for all metrics is persisted using KairosDB on top of Cassandra.

 .. image:: /images/zmon/zmon-1.png

By design the worker executes a check command targeting a given entity, where an entity is among others a host, a database, or any deployed service. A check yields a result that is in the next step passed on to a set of alert conditions, if it evaluates to true, the alert is raised. Both check command and alert condition are Python expressions, providing a powerful toolset to everyone. Every check is defined somewhere in a git repository, we are scanning known project repositories for a folder “zmon-checks” containing yaml definitions of checks. Doing so allows everyone to take care of and manage his own set of checks, without any further help, idealy. Any check can have multiple alerts that are defined using the UI and are assigned a responsible team, often the project owning team or the Incident Management team. Alerts can be cloned or inherit, making it easy to have e.g. different thresholds for different teams or change behavior by time of day.

 .. image:: /images/zmon/zmon-2.png

The schedulers and any number of workers communicate using Redis lists, the scheduler creates a JSON task, containing a check command, a target entity, and a set of alerts. This is passed to the worker, which itself consists of lots of Python processes polling the queue for new tasks. Having received a new task, the command is executed, the alerts evaluated and if necessary the alert state is changed and notifications are sent out. Using the Redis queue allows us to scale the number of workers to support the growing number of checks teams put into place. Python was initially chosen, as it not only provides a well working “eval” function, but also integrates well with lots of C bindinigs, e.g. snmp or similar system level commands. Most checks however do query application specific JSON endpoints or fire SQL queries against our PostgreSQL EventLog database.

 .. image:: /images/zmon/zmon-4.png

**Problems ...**

There were some problems along the way: We first used Celery as a task broker with Redis, however we did not manage to make it run fast enough, and in the end we did not really need a big framework if all we wanted was encode some task in JSON and fire and forget it into the queue. So Celery was dropped, significantly improving the throughput. Unfortunately this period of problems created a bad smell, that one really should avoid if trying to sell a new monitoring solution people put their trust in. Second, the scheduler is in Python, too, and with the growing number of checks and data, our implementation for scheduling combined with some cleanup tasks and background threads for refreshing data, was no longer fast enough for checks with intervals < 5s. This was solved with spawning another scheduler responsible only for checks with intervals 30s or less, yielding a much better throughput of low interval checks.

Currently we are adding more features and working on solving one big remaining issue, that is the Redis dependency in a multi data center environment. We run UI nodes in all DCs with multiple LBs, so UI will be fine and available, but the queue and state is currently a hot topic. On a prototype basis we wrapped all Redis calls, and now mirror writes to our Cassandra cluster (see charts when feature was enabled). For writing this seems to work well so far, we have a very limited dataset (scales with hosts, applications, checks) and get replication across nodes and DC for free. The results of this migration will remain open for now ...

.. _our PostgreSQL database monitoring tool: http://tech.zalando.com/posts/monitoring-postgresql-with-pgobserver.html
