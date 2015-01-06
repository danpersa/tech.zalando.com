<!--
.. title: GWT - Developer's thoughts - Part 1
.. slug: gwt-dev-i
.. date: 2013-05-02 10:00:40
.. tags: development,google-web-toolkit,gwt,java,logistics,maven
.. author: Bruno Ribeiro
.. image: gwt-logo_teaser.png
-->

As a Java Developer my work in the Logistics Team at
Zalando consists of creating functional and reliable software to be used in
our warehouses through a varied technology stack where the Google Web Toolkit
(GWT) plays an important role. This post and the following ones will focus on
GWT for enterprise software development.

I will try to share with you some lessons learned and also some of the
experiences carried out with this powerful framework.

<!-- TEASER_END -->

## GWT Introduction and Setup
Coming from a Java Swing background, the learning curve to GWT was small.
However, I quickly realized that there are big differences that must be
addressed to develop a reliable and responsive application that delivers great
user experience.

The Web is not a Desktop; that is the first thing we must
accept when starting a Rich Internet Application development (it may seem
obvious, I know, but it’s really important). Although we try to deliver a
Desktop experience to the end user, we are still running inside a Web Browser.
Having this in mind is a key factor for designing your GWT applications. One
has to know GWT capabilities but, of not less importance, also its
limitations. These limitations are worth their own post so I’ll discuss them
in the future.

I believe that user experience plays a significant role in
[enterprise software development](http://geek-and-poke.com/2010/07/how-to-make-enterprise-software.html).

In this series of posts about GWT, my goal is
to share with you some thoughts on how to leverage those capabilities and how
to overcome some of its limitations.

For that purpose we will start developing
a GWT based application from scratch; I will try to cover topics like
integration with Spring Security, UIBinder, Activities and Places, how to
modify and debug GWT-RPC calls, use REST in GWT, and other stuff that I hope
you’ll find interesting.

This first post, unfortunately, can be kind of
boring. I already introduced you to the topic and now it’s time to configure
the project. We are going to use the GWT Maven plugin (assuming you have a
functional maven installation). You can check the plugins docs on its
[homepage](http://mojo.codehaus.org/gwt-maven-plugin/) and the configuration
is quite straightforward.

We will target the latest GWT version at the time of
writing (2.5.1) and the project setup is as easy as writing in a terminal:

```bash
mvn archetype:generate \
   -DarchetypeGroupId=org.codehaus.mojo \
   -DarchetypeArtifactId=gwt-maven-plugin \
   -DarchetypeVersion=2.5.1
```

It will ask you for some definitions of the project, for which I used:

```bash
groupId: com.zalando.tech
artifactId: gwt-demo
version: 1.0-SNAPSHOT
package: com.zalando.tech.gwtdemo
module: GwtDemo
```

But, of course, you are free to use any other definitions. If everything has
gone well we should now have the skeleton of our first application, so lets
test it.

First we need a servlet container to run our application. For that we
will use the [Apache Tomcat Maven Plugin](http://tomcat.apache.org/maven-plugin-2.1/). Just edit the pom.xml in our project folder and add the
following lines inside the plugins section.

```xml
<plugin>
    <groupId>org.apache.tomcat.maven</groupId>
    <artifactId>tomcat7-maven-plugin</artifactId>
    <version>2.1</version>
</plugin>
```

Open a terminal window on our project root folder and execute:

```bash
mvn clean install -U
```

This will compile our project and download all required dependencies, so it
might take a while to complete. Next step is to finally run our application,
just execute:

```bash
mvn tomcat7:run-war
```

wait for completion, navigate to [http://localhost:8080/gwt-demo](http://localhost:8080/gwt-demo) 
and you should be able to see the following screen:

[![Hello GWT](/files/2013/04/gwt_1.png)](/files/2013/04/gwt_1.png)

This will be our starting point for the next post of this series, where we’ll add some
Spring security to make it more interesting :)

See you on the next one.

The [Google Web Toolkit](https://developers.google.com/web-toolkit/) Logo was
created and shared by Google and used according to terms described in the
Creative Commons 3.0 Attribution License.

