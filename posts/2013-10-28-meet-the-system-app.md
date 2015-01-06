<!--
.. title: The System App, yet another OS tool by Zalando
.. slug: meet-the-system-app
.. date: 2013-10-28 10:47:41
.. tags: coffeescript,development,json,mongodb,monitoring,nagios,node,open-source,platform,svg
.. author: Igor Ramadas
.. image: system-app.jpg
-->

After our handy [database utilities](http://tech.zalando.com/tag/postgresql/)
and a nifty [data management tool](http://tech.zalando.com/the-cube-app-announcement/), it’s time to officially release yet another open-source tool.
The System App is used internally at Zalando’s technology department to
provide an overview of our network and systems health. We're talking about a
diagramming tool which allows you to bind any external JSON data to its
shapes, and create visual alerts based on rules applied to this data.

<!-- TEASER_END -->

We call each of these diagrams a map, and you can create as many maps as you want. For
different purposes, showing different aspects of your infrastructure. Maps can
be created using the UI with drag-and-drop elements, or by writing a JS script
to initialize and update the map depending on your requirements.


[![System App -
Dashboard](/files/2013/10/ss_full1.jpg)](/files/2013/10/ss_full1.jpg)

The app itself runs on top of Node.js, using MongoDB for data storage and
mainly coded with CoffeeScript. The maps are presented using SVG and there’s
tons of Javascript, CSS3 and HTML5 features involved. Communication between
server (Node.js) and client (browser) is done with a mix of WebSockets and
traditional AJAX. Backbone.js and Lo-Dash completes the stack.

**The System App works with your existing data!** It can parse and query any valid JSON file on local and remote locations, meaning you can easily dump your CMDB records to JSON and use that data in the app to create maps of your services, servers and connections. The System App will take care of refreshing this data every few seconds or minutes to keep maps up-to-date, depending on your preferences.

[![System App - Audit
Data](/files/2013/10/ss_auditdata.jpg)](/files/2013/10/ss_auditdata.jpg)

Are you using Nagios? Icinga? Zenoss? NewRelic? No worries, you can bring all
this data to the System App as well. Register the JSON output locations and
bind all this monitoring data to the objects on the maps. Requests per second,
sessions per minute, CPU load, exception count... you name it. And best of
all, you can transform all that data using your own custom variables.
Variables are JS based so the possibilities are virtually unlimited.

Deploying the System App on your own hosted servers should be quite straight-
forward and can be done using our install script or Node’s package manager.
Some of you will be pleased to know that it’s also easy to deploy on the
cloud. It comes with built-in support for AppFog, OpenShift and Nodejitsu. And
it doesn’t stop there: Twitter, Loggly, MongoLab, SendGrid and Mailgun are
some of the services that can be easily integrated by changing settings on the
app's configuration file. **Get your hands on it! **So head on to
**[systemapp.io](http://systemapp.io)** for more info and a working live demo.
Any feedback is very welcome, and please let us know if you're interested in
helping us building this amazing tool :-)
