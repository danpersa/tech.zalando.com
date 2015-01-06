<!--
.. title: Breaking Up is Hard to do... or is it?: From Java 6 to 7
.. slug: breaking-up-is-hard-to-do-not-migrating-from-java-6-to-7
.. date: 2013-04-11 12:14:53
.. tags: development,java,maven,python
.. author: Rodrigo Reis
.. image: breaking-up_teaser.png
-->

With the advent of Java 7, it’s time to move on and say goodbye to
Java 6. For an extensive codebase like ours with about 400 modules, that’s a
real challenge. But, as Barney Stinson famously said, "Challenge Accepted!"
Because we’ve already had a few new projects compiling with Java 7 and using
the new language features, we were very motivated to migrate all of our
remaining projects.

<!-- TEASER_END -->

With the help of some automation - e.g. Python to the rescue! - and since we
use Maven to manage our projects, it was a matter of some lines of code to
develop a script that tests compilation (and running unit tests, of course) on
Java 7.

[![Our silly walk to Java 7!](/files/2013/03/Java-6-to-7.jpg)](/files/2013/03/Java-6-to-7.jpg)
After our first pass, great news: almost all of our
code is ready for Java 7! Code that failed just needed a few minor changes.
These minor changes were necessary because of a few incompatible JDK API
changes such as introducing a new method in javax.sql.CommonDataSource.

Overall, we managed to develop a tool that automates migration to not only
Java 7, but also to the upcoming versions. In the end, this walk [is not particularly silly](http://www.youtube.com/watch?v=IqhlQfXUk7w)!

You can check out [here](https://github.com/zalando/mjtester) the source code of our tool.

_Java is a product owned by Oracle Corporation. Monty Python is owned by
Python (Monty) Pictures Ltd._

