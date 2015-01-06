<!--
.. title: The Cube. Our data management tool just got released!
.. slug: the-cube-app-announcement
.. date: 2013-08-15 10:31:45
.. tags: backbonejs,development,javascript,node,open-source,solr,platform
.. author: Emanuel Lauria
.. image: cube_teaser.png
-->

In a fast-paced environment, Zalando's
Technology department - with more than 300 engineers, product and quality
managers - copes with a lot of different organizational and technical
entities: staff, projects, modules, servers, hosts, services and tickets.

Modern collaborative spreadsheet-in-the-cloud solutions tend to be perfectly
suited for data manipulation but very weak on data exploration. To manage our
growing set of entities, we decided to develop a clever and comfortable web
user interface called the "Cube". After months of daily usage here at the
Technology department, we now want to share it with the community; it's now
open source and available to anyone on [github](http://github.com/zalando/cube).

<!-- TEASER_END -->

The Cube is a [NodeJs](http://nodejs.org) +
[BackboneJs](http://backbonejs.org) app that takes advantage of [Apache
Solr's](http://lucene.apache.org/solr/) faceted results to organize and filter
your data. It offers a RESTful API, import scripts and managers, exporters,
authentication mechanisms (including LDAP), and a broad set of features to
manage your data like sort, filter, colorize, multiple views to present the
data and of course add, update and delete functionality.

[![THE CUBE](/files/2013/08/cube-app.png)](/files/2013/08/cube-app.png)

We have prepared a live demo where you can play with the Cube and test all
previously mentioned features. Please visit
[http://cubeapp.io](http://cubeapp.io) and give it a try! If you feel brave,
you'll find installation instructions there, too.

Like most of Zalando's Open Source software the Cube is licensed under the
Apache License and it has a [GitHub repository](//github.com/zalando/cube).
Feel free to clone, pull, create issues, push requests or do (almost) whatever
you want with it.

Developing this tool has been a fun ride and we still have
plenty of ideas to include. Improvements on the importer are underway, along
many other specialized features that will enable you to use the Cube in many
different ways. Don't hesitate to suggest your ideas and needs! We hope it's
as useful to you as it has been to us.

