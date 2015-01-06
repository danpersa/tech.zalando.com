<!--
.. title: Monitoring PostgreSQL with PGObserver
.. slug: monitoring-postgresql-with-pgobserver
.. date: 2013-05-09 12:30:02
.. tags: database,development,open-source,pgobserver,postgresql
.. author: Jan Mußler
.. image: pgobserver_teaser.png
-->

A large number of PostgreSQL databases has been serving Zalando
since fall of 2010, successfully fulfilling our requirements with its good
performance, technical flexibility, and high availability.

Today the Zalando
platform is powered by more than 25 PostgreSQL clusters, which together serve
about 5 TB of data and on the lowest layer securely store everything that
keeps the platform going. That includes a wide range of entities, such as
customers, orders, articles, and stock data. However, some data is transformed
and made available using other proven technologies that are more appropriate
for our high performance e-commerce platform (e.g., Apache Solr or Memcache).
Looking back at the past years and peeking into future of the Zalando
platform, we are very confident in the performance and flexibility that
PostgreSQL provides us.

<!-- TEASER_END -->

[![tech_blog_1](/files/2013/05/tech_blog_1.png)](/files/2013/05/tech_blog_1.png)
The following is a small sample of our use cases:
using stored procedures as an API layer between our Java software and the
database, executing queries with plproxy across distinct shards, using partial
indexes for fast queues, and using plpython to import data from non-PostgreSQL
databases. This gives us great flexibility to control and maintain efficiently
the underlying data structures. In addition, PostgreSQL's hot standby mode
provided us with easily manageable read scalability. In the extremely rare
cases of system failures, PostgreSQL has proven itself to be reliable.
Moreover, when we had to switch to hot standby systems, PostgreSQL met our
very strict demands in that service downtime was close to zero and there was
absolutely no data loss.

[![techblog6](/files/2013/04/techblog6.png)](/files/2013/04/techblog6.png)
Back in 2010, Zalando started with a promising
PostgreSQL 9.0 RC1, today we maintain clusters spanning from 9.0 to the most
current 9.2 release. Improvements in the latest versions are highly
appreciated (e.g. concurrent creates and drops of indexes, improved CTE
functionallity and better statement monitoring). Unfortunately, migrating to
new major versions remains problematic in many cases due to the downtime that
is required for the upgrade.

[![techblog3](/files/2013/04/techblog3.png)](/files/2013/04/techblog3.png)
Monitoring all of our clusters and a large
number of stored procedures and queries is a challenge. However, it is
essential for guaranteeing continuous high performance on our shopping
platform. Because we were unhappy with the tools that were available back
then, we went our own way in monitoring key indicators on our PostgreSQL
database servers -- tracking CPU load, database growth, and stored procedure
performance metrics in particular.

Therefore, we would like to introduce our
tool, called "PGObserver", to you. Time and time again, it has proven to be
incredibly useful to have detailed historical performance data available
whenever you are trying to pinpoint bottlenecks or performance degradation. It
also enables better analysis of database performance tests and future system
planning and it provides developers with a more accurate picture of the
importance of code they are touching.

[![tech_blog_2](/files/2013/04/tech_blog_2.png)](/files/2013/04/tech_blog_2.png)
PGObserver consists of two applications: a Java data gatherer process and a web frontend written in
Python. We did not try to build a general time series database. That's because
our focus at the time was -- and remains to this day -- to explicitly track
the available PostgreSQL performance metrics, including some relevant system
metrics. Currently, PGObserver can be configured to track the following key
data on a per system per metric configurable time interval:

  * Stored procedure performance metrics (number of calls, run time, self time)
  * Table data (growth, index scans, sequential scans, […], inserts, deletes, updates)
  * Table I/O data (heap and cache hits)
  * CPU load (through a plpython stored procedure)

[![techblog4](/files/2013/04/techblog4.png)](/files/2013/04/techblog4.png)
Individual per system configuration enables you to limit the amount of
data gathered and stored if necessary, but at the same time it also gives you
the means to increase the resolution for more interesting and critical
systems.

In the future, we will continue to work on PGObserver to improve its
usability, to expand its feature set, and to remove a few shortcomings. But
since we have already benefited a great deal from it, we believe it is time
that others may do, too. So check it out on
[github.com/zalando/pgobserver](http://github.com/zalando/pgobserver) and get
back to us with your feedback.

