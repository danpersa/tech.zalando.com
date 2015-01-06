<!--
.. title: Introducing Technology's Zooport
.. slug: zooport
.. date: 2013-08-20 10:00:47
.. tags: database,dba,development,support,sysop,test-engineering,testing,zooport,platform
.. author: Enrico Hartung
.. image: zooport_teaser.png
-->

Zooport - internal support for Zalando technology teams With a continuously
growing Technology department and therefore a technology stack which is
expanding with a steady pace, sharing knowledge becomes a real challenge. Thus
the need for internal support is high. With the Technology Zooport we
introduced internal support for all our engineers, testers and product
managers working in the Technology department.

<!-- TEASER_END -->

Before Zooport it was common
practice to simply walk over and ask others for help. This was O.K. back when
we were less than a hundred people working in software development. However we
are now in the hundreds, and this became a denial of service attack against
our more experienced employees.

In order to overcome the flood of support
requests, prevent getting lost with helping others, and blocking work on
projects or new features our teams started to look for ways out. As a result
several mailing lists, ticket systems and group chats were introduced. Some
teams even bought toy animals for labeling the employees people could go to.
All this made dealing with the requests easier for the supporting teams, but
caused confusion for those who were seeking support. It was unclear whom to
call in which way for which kind of issue.

Hence we took all of these
different approaches and brought them together in a distributed internal
support where technology teams give support on particular topics to other
technology teams. Due to the toy animals of some teams we named this project
"Zooport".

[![All animals of the Zalando Technology Zooport](/files/2013/08/zooport2.png)](/files/2013/08/zooport2.png)

## Meet the Zooporters

The first rule for participating in the Zooport is that each team has to name
an animal as its alias. This animal is supposed to mark the team member who is
on duty, can be contacted for requests and who is working on the issues in our
Zooport ticket system. Everyone on duty is called "Zooporter". We started our
zoo with four animals, but more are about to join. [![The Zooport toy
animals](/files/2013/08/zooport_toy_animals.jpg)](/files/2013/08/zooport_toy_animals.jpg) The Zooport toy animals
[![The Zooport animals built with Lego](/files/2013/08/zooport_lego_animals.jpg)](/files/2013/08/zooport_lego_animals.jpg) The Zooport animals
built with Lego

### Elephant

[![The elephant represents the database administrator on Zooport duty](/files/2013/08/elephant.png)](/files/2013/08/elephant.png) 
It all started
with the blue toy elephant from our database administrators (DBAs), which was
inspired by the PostgreSQL logo. It represents our DBA on Zooport duty. Our
database administrators are popular people and they used to receive a lot of
support requests from chats, email or by direct approach. Each of these
requests caused a disruption of the DBA's work and it wasn't that unusual that
several DBAs were contacted with same issue if one didn't answer fast enough.

Now the DBA on elephant duty is the only one answering database requests and
giving ad-hoc support on SQL queries. This allows our other DBAs to
concentrate on their projects as well as on their planned development or
consulting tasks.

### Turtle

[![The turtle represents the platform engineer on Zooport duty](/files/2013/08/turtle.png)](/files/2013/08/turtle.png) 
Shortly afterwards other teams took up this
idea and soon a green turtle was introduced representing our platform software
team. In the Discworld novels by Terry Pratchett the world rests on the back
of four elephants which are standing on a giant turtle, in case someone
wonders about the connection between a turtle and our software platform. 

The developer on turtle duty is responsible for all kinds of support requests
regarding our internal tools and infrastructure. This also includes central
components of our production environment. Typical tasks are setting up
services on our cloud infrastructure, granting access to our tools and giving
deployment permissions. Besides this the turtle is managing the bug reports
for our shared tools, components or libraries. Furthermore, all requests
related to our continuous delivery infrastructure are sent to the developer on
turtle duty.

### Penguin

[![The penguin represents the system operator on Zooport duty](/files/2013/08/penguin.png)](/files/2013/08/penguin.png) 
The Zalando ZEOS platform runs on Linux, so
what is more obvious than having one of our system operators (sysops) on
penguin duty. Thus whenever a new virtual machine on our cloud infrastructure
is needed, someone is lacking access to our networks or some configuration
change on the production environment is needed the penguin is in charge. 

He is also ordering new hardware and answering questions regarding the status of our
technical infrastructure. Furthermore the sysop on penguin duty can be
contacted on all issues concerning our environments on the operating system
and network layer.

### Koala

[![The koala represents the test engineer on Zooport duty](/files/2013/08/koala.png)](/files/2013/08/koala.png) 
The newest animal in our zoo is a friendly koala bear
acting as the ambassador of our [test engineers](http://tech.zalando.com/test-engineering-at-zalando/). 
Why a koala? Well, test engineers belong to our QA
and are also called “QAlers” ... The koala duty spans support and
administration of our test environments and test tools as well as support for
our automatic system tests. Moreover, the koala is responsible for analyzing
and managing bug reports regarding the tools developed by our test engineers.

He is the one, our testers and test engineers go to if they need help, but
more and more developers have been seen in the waiting line at the koala desk,
lately. 

Since our Technology department is continuously growing more and more
animals are arriving in our zoo, e.g. rumors about a German Shepherd giving
support on security issues are already going around.

## Zooport tools

[![Zooport view in team cube](/files/2013/08/Cube-Zooport.png)](/files/2013/08/Cube-Zooport.png) 
With a click on the paw icon in our team cube one can see who is currently on Zooport duty All our Zooporters
can use a set of tools we set up to support them on their duty. The main tool
is JIRA, our ticket system, in which we have defined several ticket types
according to the main tasks of our Zooporters, e.g. create an account for our
internal tools, request a new virtual machine in our cloud or the setup of a
new component on a particular environment. For each ticket type we can
implement a customized workflow in case extra steps like an approval are
needed. We also provide dashboards, daily as well as weekly email reports on
the status of open tickets and the possibility to escalate tickets. Our
employees on duty can be contacted over a group chat and by direct approach,
they can be recognized by the corresponding toy animal. Since not everybody
wants to walk over to the team in order to check who's on duty, they are
labeled in our [Technology team cube](http://tech.zalando.com/the-cube-app-announcement/), too. 

Although the toy animals might provoke a different view,
we are taking our internal support seriously. All task types have SLAs for the
first response and the resolution time which we are monitoring with daily and
weekly reports. We already have a lot of ideas for extending our Zooport and
increasing the quality of our internal support.

