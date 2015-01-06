<!--
.. title: Getting a quick view of your PostgreSQL stats
.. slug: getting-a-quick-view-of-your-postgresql-stats
.. date: 2013-07-22 17:57:57
.. tags: backend,database,development,open-source,pg-view,postgresql
.. author: Oleksii Kliukin
.. image: postgres-stats_teaser.png
-->

Database health monitoring is important, especially if you are running your
servers 24x7 and aiming for no downtime. There are a number of tools to show
interesting database-related statistics in a pretty web interface, from home-
grown solutions based on Nagios or Zabbix to specialized web apps; one of
them, [PGObserver](https://github.com/zalando/PGObserver), is developed by our
colleagues at Zalando. On other occasions one needs a detailed real-time view
of the database and system metrics that can be launched from the terminal: for
instance, a DBA might want to monitor system load, query locks and I/O
utilization during the lengthy data migration. Previously, we used a
combination of  Linux system utilities like uptime or iostat, information from
/proc and data from pg_stat_activity put together as a shell alias. But
nowadays we have something more powerful, a new tool called pg_view.

<!-- TEASER_END -->

[![pg_viewscreenshot](/files/2013/07/pg_view_shot.png)](/files/2013/07/pg_view_shot.png)

pg_view’s basic idea is to combine the indicators commonly displayed by sar or iostat
with the output from PostgreSQL process activity view to present global and
per-process statistics in a way that is easy to interpret on a quick glance.

The default output includes every database running on the current host. For
each of them, various measurements for the xlog and data partitions are
displayed, as well as the combined output from pg_stat_activity and process
information, i.e. read/write rates in MB/s, processor time spent in system and
user mode, unix process state and some other details. The upper part of the
screen contains overall system statistics, like the CPU utilization, memory
used/available, host uptime and other parameters typically included in the
top-like monitoring utilities.

With the help of ncurses module, pg_view
highlights problematic values to be instantly noticeable by a DBA. For
example, on the screenshot above the query waiting on a lock is highlighted in
red, indicating a potential problem, and the idle in transaction status is
displayed in blue (warning). Both of those conditions may lead to overall
performance decrease and unplanned maintenance. The indicators that require
immediate attention are also shown in red, i.e. the fact that the data
partition will be full in just a couple of seconds is highlighted.

The curses library also provides necessary facilities to make the interface scalable, so
one can view multiple hosts at once on a split terminal screen or have a small
window open for a mission-critical database to keep an eye on it at load
peaks. We tried to keep the system requirements reasonable, opting for Python
2.6 and PostgreSQL python adapter psycopg2 as the only external module. At the
moment, the script relies heavily on the /proc/ filesystem, meaning that it
only works in Linux environment.

Among the many features pg_view has an
ability to switch its output to a plain text or json format, so the data
collected can be processed by other applications. The script is designed to be
extensible: adding other output methods (i.e. storing results in a database)
shouldn't be a problem. The best part, of course, is that it is the latest
addition to the growing Zalando open-source toolchain:

  * pg_view -> [github/zalando/pg_view](https://github.com/zalando/pg_view)
  * PGObserver -> [github/zalando/pgobserver](https://github.com/zalando/pgobserver)
  * Java-sproc-wrapper -> [github/zalando/java-sproc-wrapper](https://github.com/zalando/java-sproc-wrapper)

