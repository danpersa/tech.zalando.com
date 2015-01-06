<!--
.. title: My three year journey into Zalando Technology
.. slug: my-three-year-journey-into-zalando-technology
.. date: 2013-09-30 14:00:04
.. tags: anniversary,birthday,platform,tech-diary
.. author: Henning Jacobs
.. image: zalando-birthday_teaser.jpg
-->

This week we celebrate Zalando's 5th
anniversary. Zalando is one of the biggest success stories in the internet
history, becoming Europe's fastest growing company, ever. Especially from a
tech perspective we have been through a real rollercoaster ride — with an
exceptional pace, always a pulse at 180 and a whole lot of fun.  I am very
proud of our tremendous achievements and very thankful for having such an
awesome team working together on all past and future challenges. And now I
want to leave room for Henning, one of our "Oldies", to give quite an
impressive overview of our ride out of his tech diary. _Christoph, CPO_

<!-- TEASER_END -->

## Early 2010: Magento
**2 deploy units, > 800k PHP LOC**

When you get a call from a headhunter asking you whether the job position "PHP developer using Magento" sounds interesting to you — say no!

But I said yes, so here the story begins: I got back from South America just before Christmas 2009 and started looking around for jobs in Northern Germany when the aforementioned call arrived. I was tempted to decline the offer as I had some (bad) experience with Magento in Argentina — but why would I ignore the possibility to go to Berlin and get some more interview experience? So I showed up in cold, snowy, dirty Berlin in January 2010.

Having used mainly C# and PHP professionally I wanted to switch to Java as I considered PHP an inferior language and the C# environment meant Microsoft hell. To be honest, I knew little about Zalando. However, the planned switch from PHP to Java (which I was eager to use professionally) and the welcoming people convinced me to accept the offer given to me just after the interview. 

The first weeks and months were dedicated to getting into Zalando’s Magento PHP code and evaluating some frontend technologies for tools. As no dedicated System Engineer (SysOp) was onboard, I somehow was given the SysOp role along with another colleague. I was therefore tasked with trying to keep up the small Apache/PHP and MySQL server farm. PHP changes were either deployed via Bash scripts (after creating a SVN tag) or PHP files were directly edited on the server. With a small team of not more than ten developers this was feasible, but still bad. Somehow — I do not remember exactly how — I was given the task to evaluate GWT and as Java was already in use for internal tooling, we decided to go forward with GWT for our existing and future frontends. [![ZEOS evolution 2010-2013](/files/2013/09/Zalando-Evolve-2010-2013-w200.png)](/files/2013/09/Zalando-Evolve-2010-2013-w200.png)  

## Spring 2010: "Booster"
**4 deploy units, > 900k PHP LOC**

The increasing success and traffic was showing us the limits of Magento and patching/fixing the shop to keep it running was a daily challenge. The shop frontend already had a full frontend cache using Memcache to store rendered HTML, but cache misses were leading to dramatic page load times with about 120 MySQL queries trashing the MySQL slave DBs for only one catalog page load. Parallel to our efforts to scale the shop frontend, a colleague was working on replacing an external (paid) product search with a custom solution based on Apache Solr.

His intention was to use Apache Solr purely as a full text search engine to return article SKUs (product identifiers). As our efforts to scale the faceted catalog pages with MySQL were not leading to any fruitful results, we decided to join the search engine colleague’s Solr endeavours.

That’s how our shop frontend still runs after three years: all article/product information is served by a cluster of Solr servers and no DB queries are issued on catalog pages.

The project of replacing Magento’s catalog rendering with our own scalable solution was called "Booster" and is probably the most successful and satisfying project I have ever done at Zalando. After just one week of prototyping with a team of four, and one week of cleaning up messy corners, our improvements (which basically meant replacing the whole catalog rendering) went live.

But the Booster project was just a tiny hint of what came next: the Zalando "Reboot".  

## Summer/Autumn 2010: "Reboot"
**7 deploy units, > 200k Java LOC, > 200k SQL LOC**

Our Magento PHP stuff — especially now the checkout part — was falling apart everywhere you looked. Non-unique order number reservations was just one special "feature" of the Magento code. The decision was not only to rebuild the shop (which might have been easily done with PHP again), but to rebuild everything from scratch in a completely different setting with Java and PostgreSQL. The technology change was dramatic: PHP to Java, one webapp to multiple Backend components, non-threaded PHP to JVM concurrency, and last but not least, basic MySQL to advanced PostgreSQL with stored procedures. Besides Java, we were also introducing Python at that time as our workhorse for scripting, internal tooling and system administration tasks. With Java+Postgres+Python you can get pretty far :-)

The new Zalando technology setup had four big components, namely the new Java Shop (using Stripes as MVC framwork), the SOAP providing Customer Service (Java Webapp), the "Business Master" (Java Webapp) and a customized ERP system. All our shiny new Java components had a common setup with Maven as the build tool, Tomcat as the web container and PostgreSQL as the database with stored procedure access. We also took the opportunity to lay the basic foundations for Continuous Integration with Jenkins ("one unit test is infinitely better than no unit test").

September 2010 — when all those components went LIVE — our Zalando eCommerce Operating System (ZEOS) was born. Switching from Magento PHP/MySQL to our custom platform was a major effort especially with all the data migrations from MySQL to PostgreSQL. With several sleepless nights, we managed to switch over with only 90 minutes nightly downtime. Don’t ask about the backlog of issues we had to fix still months after the actual "Reboot" switch ;-)  

## Year 2011: Expansion
**10 deploy units, > 700k Java LOC**

During this time I was partly still a SysOp, partly DB Engineer (designing some of the DB structures still in use 2013) and partly shop developer. In terms of being a shop developer, 2011 was the year of internationalization. We rolled out the Netherlands and France already end of 2010 — Italy, Great Britain, Austria and Switzerland followed 2011. Expansion not only meant rolling out new countries but also benefited German customers as we introduced our Partner Program with tons of additional products for our shop. Furthermore, a shop relaunch with completely new category management was done.  

## Spring 2012: ZEOS phase 1
**20 deploy units, > 900k Java LOC, > 150k SQL LOC**

Rolling out an ERP system 2010 was a big step forward but introduced new dependencies and constraints which needed to be resolved in 2012. Our increasing order volume (>1 billion EUR net revenue in 2012) was just too challenging for the proprietary ERP running with just one (very) big Oracle database. The next logical step was replacing the ERP with new ZEOS Java components, that could be relied upon to constantly handle our increasing amount of orders.

For this so-called "ZEOS phase 1" project, I had to get into the order processing flow, which I had not seen too much of (being SysOp and Shop developer) until now. In the short time frame of about three months, we managed to completely extract the order related processing from the ERP system into our own new ZEOS components (Java/Tomcat/PostgreSQL). We managed to show that our new setup could easily scale to handle ten to hundred times the order volume of that time (March 2012).  

## Since 2012: Platform
**> 100 deploy units, > 3M Java LOC, > 1M SQL LOC, > 150k Python LOC, > 600 Maven artifacts**

Having been around different teams (SysOp, Shop, Order) and handling tasks related to monitoring and deployment, I somehow became the "platform" person providing infrastructure to other teams. In Autumn 2012, this platform idea was transformed into a new "Platform" team structure. The "Platform" team provides all necessary Technology infrastructure to other feature/topic oriented teams: System Engineering, Database Engineering, Platform/Software Engineering and Security Advisory. We are currently always working on platform improvements like server virtualization, access management (LDAP/Kerberos), continuous delivery and common tools and libraries.

Having been in different teams, I can say that I saw quite a lot of the different facets of Zalando Technology. Even with this experience, the increasing complexity makes it practically impossible to keep an overview on the whole ZEOS landscape. This is probably the biggest challenge we have to cope with as a company that has grown so fast — but solutions like semi-automated architecture documentation are underway.  

## Learnings

What did I learn (technology-wise) in the last years at Zalando? I’ll try to
summarize in simple bullet points - purely experience-based and only
reflecting my humble opinion:

  * **Be productive - delete code!** — Unused or overly long and/or complicated code is a headache especially after many changes like we have in the ZEOS codebase, however sadly the fear of losses or defects is widespread. To prevent losses we have SCM, and to prevent defects we have tests, code reviews and experienced colleagues to ask. It seems to be counter-intuitive, and naturally only a few developers enjoy cleanup tasks, but deleting code is the most productive job in my eyes and we should invent developer awards for "top code erasers" ;-)

  * **Never underestimate the lifetime of workarounds** — when I started at Zalando I would never have guessed the growth we underwent over the last years —  solving problems in 2010 was quite different from how we (mostly) approach things now. All these quick hacks and workarounds from the past still haunt us sometimes. The "undocumented" and "non-standard" type of solution is a particular type of boomerang: of course editing just one file on one production server is much easier and quicker than using configuration management (Puppet) - but it will come back and hit you hard in the end!

  * **Ensure data quality with constraints and validation** — the importance of correct data (whether it is customer information or server inventory) can not be underestimated. If you create a database TEXT field without constraints, you can be pretty sure that one day you will get unexpected contents (1 MB in a name field, various non-allowed characters, …). I once read an article about the end of the database as the centre of the company - but I would never trust important data to systems that don’t have the availability of strict constraints (such as MongoDB). Having PostgreSQL in Zalando with good constraint support (and sprocs and triggers and ..) helps — but you also have to actively use them — always!

  * **Avoid caching if you can and scale horizontally** — Caching is hard and leads to hard-to-find issues. When moving from PHP to Java we tried to exploit the Java in-memory caching possibilities as DB queries were considered "slow". After numerous and ongoing caching issues, nowadays we shard a lot, and use direct DB access through stored procedures where possible. From my experience caching often is just one form of pre-mature optimization (the "root of all evil").

  * **A homogeneous technology stack makes many lives easier** — SysOps only have to care for one production setup; new colleagues only learn one module and they theoretically know them all; the landscape can easily be explained to incident support team members or other non-developers and a common toolset (deployment, monitoring, ..) can be continuously improved and serves everybody. Having a small set of proven technology solutions (which have to be extended when necessary) works and scales better than trying to start every project with a new "optimal" technology. Singular non-standard solutions can bite you (see point 2).

## What’s next?

With its 5th birthday Zalando is becoming a "grown-up" and sometimes you can
even hear colleagues talking about "enterprise tools" in the hallways. The
technology department underwent a lot of transitions and the environment
nowadays is far different from the buzzing start-up feel in 2010. Being with
the company since 2010, I can say that we managed pretty well to neither get
lost in chaos nor in enterprise policies. Now we are nowhere close to running
out of work in my Platform area and have to tackle all the important projects
postponed during the hot growth phase: process improvements, private cloud,
access management, continuous delivery improvements, infrastructure tooling
and more.

Life at Zalando Technology will stay more than exciting :-)

