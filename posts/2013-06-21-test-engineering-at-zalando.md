<!--
.. title: Test Engineering @Zalando
.. slug: test-engineering-at-zalando
.. date: 2013-06-21 12:00:18
.. tags: automation,bdd,continuous-integration,cucumber,selenium,test-engineering,testing,testing
.. author: Enrico Hartung
.. image: test-engineering_teaser.jpg
-->

Recently at Zalando Technology the new role _Test Engineer_
was introduced into our development teams. It fills the gap between developers
and testers and thus our quality assurance has been given programming power.

Beforehand test tools and automatic system tests were provided by a central
support team found outside of the development process. Hence new tests were
requested from this team. Furthermore, information on software changes had to
be communicated between development teams and the support team in order to
interpret and update failing tests. This was not the way we wanted to develop
software, this was not agile. Now the automatic system tests are maintained by
the development teams themselves.

<!-- TEASER_END -->

## Test Engineers Improve Automation

[![Testers and test engineers at Zalando Technology](/files/2013/06/qa_small.jpg)](/files/2013/06/qa_small.jpg)

We, the test engineers, are software developers with a passion for testing.
Unlike other developers in our teams we are not implementing new features. We
are working on possibilities to test the software components of our teams in
an automatic and agile fashion.

With our work, we are contributing to the
agile software development process at Zalando, because agile development
demands a high grade of automation in order to deliver software continuously.
This doesn’t only count for the build and deployment process, but also for the
testing of software.  A high coverage with automatic tests allows testers to
concentrate on verifying new features instead of spending a lot of time doing
regression testing.  Furthermore, the automatic system tests provided by test
engineers can be used to give developers early feedback on code changes, since
they can be executed during all steps of the development process.

## Test Engineers Complement Teams

[![Test engineer in a development team](/files/2013/06/Test_Engineer_in_Dev_Team.jpg)](/files/2013/06/Test_Engineer_in_Dev_Team.jpg)
We are not supposed to replace the testers in our development
teams, but to work side by side with developers, testers and product managers
in order to develop high quality software and to assure that new features can
be delivered as fast as possible.

Our testers are experts in verifying new
features and improvements, as well as analyzing incidents since they often
know our system and processes better than anybody else. When a new process is
introduced, or a big project comes to an end they are organizing and running
the acceptance tests.

Test engineers on the other hand might think like
testers but in our heart we are still programmers. Therefore test engineers
are responsible for automating test cases, for the monitoring and
administration of our test systems and test tools, for running automatic
security and performance tests, and evaluating the results afterwards. We also
maintain the test data our testers need, to do their job. Beside automatic
tests, test engineers also develop tools which make the lives of our team
members easier.

## Test Engineers Write Code

The tools used by test engineers are the same used by developers. If we are
testing a Java application we are of course using Java frameworks and tools to
test this application. When we are writing tests for a web application, we,
for example use JUnit with Webdriver and run the tests with a continuous
integration server on a [Selenium Grid](http://code.google.com/p/selenium/wiki/Grid2). 
We even have unit tests
for the system tests, and use tools like [PMD](http://pmd.sourceforge.net/) or
[Findbugs](http://findbugs.sourceforge.net/) in order to improve the code
quality of our tests. Furthermore, the code of the system tests is organized
in models, views and controllers
([MVC](http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)) so
that test logic can be shared between different teams. Last but not least we
were the first at Zalando to develop behavior-driven
([BDD](http://en.wikipedia.org/wiki/Behavior-driven_development)) with
[Cucumber](http://cukes.info).

Test engineering at Zalando combines software
testing and software development. It is an important part of our goal to
develop software agile and deliver it continuously.

