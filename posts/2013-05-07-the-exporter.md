<!--
.. title: The Exporter
.. slug: the-exporter
.. date: 2013-05-07 10:00:18
.. tags: draft,article-exporter,backend,csv,development,exporter
.. author: ToDo
-->

There are many reasons to have a XML or CSV file containing the whole catalog
from Zalando. Some people at the company use them to create different reports,
and our partners use them to show our products on their websites (e.g. price
comparison websites). It is true that a person can manually create these files
and scroll through the company's huge catalog and start filling up an Excel
file themselves. However, here at Zalando Technology it’s all about
efficiency. We’ve developed a program that creates the desired files: the
Exporter.

<!-- TEASER_END -->

Based on our own Quartz Job-Framework, the Exporter starts itself every 15
seconds multiple times, creating different threads that process the data for
different countries. Using the same articles’ Solr search engine as the shop,
every exporter’s job reads a large amount of article data in a few seconds.
These articles are always up to date.

When it’s about writing the article's information, each job divides it’s
assigned files into different threads. These new threads iterate through the
articles, previously read and depending on the file configuration, they write
the desired attributes.

By grouping some of these jobs, and creating a 2 dimensional ID-schema we can
also parallelize the Exporter to create different threads, depending on each
country's needs (some countries may need more files than others). It is
possible for different jobs to work in the same country without their results
colliding and overwriting a file. This strategy allows us to escalate to 2
dimensions.

Today we are creating more than 400 files, for 17 shops (including
[Emeza](http://www.emeza.de) and [Kiomi](http://de.kiomi.com)), with more than
200k articles each, in an average of 40 minutes. I guess a little bit faster
than a person would take to do it.

