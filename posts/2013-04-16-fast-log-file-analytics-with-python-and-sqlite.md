<!--
.. title: Fast log file analytics with python and sqlite
.. slug: fast-log-file-analytics-with-python-and-sqlite
.. date: 2013-04-16 09:07:44
.. tags: logistics
.. author: Carsten Pohl
.. image: log-file-analytics_teaser.png
-->

_'Carsten, do you have 5 minutes?'_

Sometimes work friends need small analytics jobs doing. Every time I hear 'do you have five
minutes?', multiple log files have to be cross referenced because sometimes
they need a bit more context than that what is easily possible with the
trusted shell-all-star-combo of find, grep, sort and cut.

As an added wish,
they'd be very happy if the result could somehow be worked on via SQL because
there are already a lot of written SQL statements, professional SQL analytics
tools or plain SQL blueprints out there, which help to get to the core of
critical information without reinventing the wheel. In other words : 'If I
could get this data out of these log files in my SQL database in the next half
hour, that would be great.'

<!-- TEASER_END -->

For these cases, I rely on an old, battle-proven tool chain. Python and
SQLite. The split is always the same:

  * Use python for file discovery, unzipping, data reading, context analysis and writing in the database
  * Use sqlite for organizing the data and fast analysis. Sometimes for exporting the data to a .sql or .csv file

In this short blog post, I would like to show you a setup that will help you
analyze log files in more or less five minutes.

## The python part
Python has some nice ready-for-action components. For example parsing of date and
time components. Lets say, you write a small log analysis script, and you want
that the user can give a certain date as a parameter. In that case, you can
start complicated regular expressions, or you can just use strptime. This
method can parse the given string in the time format you desire. Lets say you
want to parse dates in the format yyyy-mm-dd. You can call strptime with the
format %Y-%m-%d . If the given string cannot be parsed, a ValueError Exception
will be thrown.

```python
import time
exampleTimeString = '2013-13-31'
try:
    time.strptime(exampleTimeString, '%Y-%m-%d')
except ValueError:
print "The date is not valid"
```

The date example above will throw an exception
because strptime doesn't check the date's format, just whether the date is a
valid date or not. There isn't a thirteenth month so the date is invalid.

Another small little helper module is called gzip. Often, log files from some
services or daemons will be compressed with gzip after a certain amount of
time. With the methods provided by the gzip module, you can open the zipped
file as simply as you would open any other non zipped text file. In other
words, you can simply open the file with file = gzip.open(myZippedFile, 'rb')
without having to worry about where to temporarily store the unzipped data or
anything like that. You can read the zipped file now similarly to how you
would read from a non zipped text file.

```python
import gzip
try:
    with gzip.open('my_cool_log_file.log.gz','rb') as thezippedfile:
        workWithTheFile(thezippedfile)
except IOError:
    print "IO Error, the file probably does not exist"
```

Often, log files adhere to a certain
format, meaning that entries may be separated by tabs or other characters.
Sometimes, the log files look more like a comma separated value file (csv), in
which case another python module can help. With the csv module and some
csv.reader(yourfilehandle) magic, you get a reader object which helps you walk
through your log file because the reader object supports the iterator
protocol. While opening the csv file, you can define a delimiter like \t if
the values in your log file or your csv file are separated by tabs.

```python
import csv
reader = csv.reader('my_cool_logfile.log', delimiter='\t')
for line in reader:
    cursor.execute("INSERT INTO ... (?)", (line[0],))
```

After all that's done and when you've found the correct files, opened them and read
a lot of the data, you are ready to stuff all your findings into the sqllite
database you can ORDER, count and GROUP BY to your heart's content.

## Bringing SQLite into the mix
All you need to create your own database in
python is to import the sqlite3 module and then "connect" to a file. It works
like this: sqlite3.connect('analytics.sqlite').

If you just want to create the
database in memory, you can use the special file name :memory:. In this case,
no file will be created but the database will be stored in the system's memory
that's running the python script. After getting a cursor, you can easily
create tables and insert data, using the standard SQL CREATE and INSERT
commands. Once you've inserted everything, don't forget to commit to the
connection and close the cursor and connection.

```python
import sqlite3
con = sqlite3.connect(':memory:')
cur = con.execute("CREATE TABLE bla...... ")
cur.close()
con.commit()
con.close()
```

After that, if you chose not to
create the database in memory, you have a single file that you can copy
anywhere and open with the sqlite3 command line tool. The next steps are often
to export the SQL data to a more generic format, which you could import again
in postgres. This is often done by using comma separated value files (csv),
but sometimes you can create a sql script file, which consists of a long list
of SQL commands.

In the sqlite3 command line client, there are internal
commands to achieve this.

One way would be to decide in what format you want
to create your log, for example .mode insert to create insert statements then
start logging with the .output <filename> command and then output the schema
with .schema mytable and output the data with .dump mytable.

```python
sqlite3 carsten.sqlite
.mode insert
.output /var/tmp/import_me.sql
.dump
.quit
```

The sql file you created can be imported to postgres using the psql
command using the -f parameter.

Apart from all of that, you can call your
normal analytical queries directly in the sqlite3 command line client.

I personally find the combination of getting the data using python and analyzing
it using sqlite the best but you can swap and change the parts of this dynamic
duo to your liking. For example, sqlite can be accessed via php or perl.

