.. title: AngularJS in a Java World
.. slug: angularjs-in-a-java-world
.. date: 2014/04/16 10:14:00
.. tags: angularjs
.. author: Aike Sommer
.. image: angularjs-logo.png

My name is Aike and I work for the Tooling team of the Zalando Technology department - our job is to create applications for internal use in other teams. A little
while ago, we decided to evaluate some new technologies for our applications. One of those technologies - and eventually the one that we went for - was AngularJS.
We have since based some new applications on Angular - and other teams of Zalando Technology have just recently followed in this direction. But as quickly as we
fell in love with Angular, we also realized that there are some challenges to be tackled.

.. TEASER_END

Before we started with Angular, all of my teams frontend development was based on SmartGWT, using the MVP-pattern. This allowed us to use Java for “everything” - and
enabled us not only to develop and structure our code like in any other Java-GUI-framework, but also to use the great support of Java-IDEs. Moving away from this, we
were suddenly involved with a few technologies that we just not had that much experience with.

The biggest challenges for us were:

* Integrate all those new technologies into our Maven-based build
* Find a structure that helps us in creating not only great applications - but also maintainable and reusable code
* Understand some performance relevant internals, helping us push the limits just a little

In this post I want to focus on the structure that we are using for our applications.

Structure that code
-------------------

Angular defines a few types of application-components: controllers, services, directives and filters are mostly written in JavaScript, the template itself is plain
HTML with some additional markup. When following some basic principles, it is usually quite obvious whether a piece of code belongs into a controller, a service or
any of the other types. This leads to many Angular-based applications having a big template and a few JS-files: controllers.js, services.js and so on. For simple
applications this is actually working quite nicely.

When applications grow a little bigger - and especially if multiple developers are working on the same code-base - the first step is usually to split these files
into smaller ones inside of corresponding directories. This does help in avoiding merge-wars because of multiple developers working on the same files. Some other
downsides of a growing code-base might also be easy to fix or simply not worth the effort to come up with anything else.

But in the end the developers will still waste lots of time searching. Devs will have to search for the definition of some method or field available on the $scope,
a specific controller or service or for the template or stylesheet that corresponds to some part of your application. In any case the question will be “Where is the
code, that causes this behaviour?”. As JS and especially Angular support in current IDEs is just not as far as it is for Java - and also because of the dynamic
nature of JS - your IDE will only get you that far in helping you with your search.

Another reason for a good structure of your code is the reverse question “What happens, when I change this code?”. Especially when working with very large
controllers, possibly even across multiple views, side-effects can be very hard to trace. A usage-search on some $scope-method will in many cases just not give you
the expected result.

Same logical structure on all levels
------------------------------------

To make our code maintainable, we try to come up with a logical structure to our frontend (based on mockups and known requirements), that we then map onto all levels:

* DOM elements and ids
* folder- and file-names
* Angular views
* Angular component naming
* Angular scopes

To explain this, I will use a real world example - the project which I am currently most involved in: the Campaign and Media Planning tool (short: CaMP) for our
marketing department. The UI consists of 3 views (for now) - the campaign-plan, media-plan and production-plan. All those views look very similar - a header
including top-level navigation and a filter-bar on top and an overview of the corresponding entities below. A detail-view of those entities can be opened on the
right side next to the overview-area.

For each of those views, we create a folder named by the view (/app/campaign-plan) and a template main.html inside of it. The root-element in this main.html gets
the name of the view as id and an ng-controller-attribute with the camel-cased name of the view (<div id=”campaign-plan” ng-controller=”CampaignPlanController”>).
This controller is then also created inside of the views folder (/app/campaign-plan/CampaignPlanController.js). For styling of this view, a LESS-file
/asset/less/campaign-plan/main.less is created, which is completely scoped to the root-element of the template (#campaign-plan { ... }).

The view is then further divided into logical areas. One of those is for example the detail-area on the right edge. For every such sub-areas a template
(/app/campaign-plan/detail/main.html), an id (campaign-plan-detail), a controller (CampaignPlanDetailController) and a LESS-file (/asset/less/campaign-plan/detail.less)
is created.

The way the controllers are attached to the DOM-elements, the Angular scopes are automatically created in that same structure. For things like services, directives,
filters and other components used by multiple views, there is also a folder /app/common.

In the end we have something like this:

.. image:: /images/camp-mock-areas.png
   :width: 100%

|

+------------------------------------------+------------------------------------------+--------------------------------------------------------------+
| Logical Path                             | DOM Element                              | Controller                                                   |
+------------------------------------------+------------------------------------------+--------------------------------------------------------------+
| Template File                            | LESS File                                | Controller File                                              |
+==========================================+==========================================+==============================================================+
| /                                        | body                                     | CampController                                               |
+------------------------------------------+------------------------------------------+--------------------------------------------------------------+
| /index.jsp                               | /asset/less/main.less                    | /app/common/CampController.js                                |
+------------------------------------------+------------------------------------------+--------------------------------------------------------------+
| /campaign-plan                           | #campaign-plan                           | CampaignPlanController                                       |
+------------------------------------------+------------------------------------------+--------------------------------------------------------------+
| /app/campaign-plan/main.html             | /asset/less/campaign-plan/main.less      | /app/campaign-plan/ CampaignPlanController.js                |
+------------------------------------------+------------------------------------------+--------------------------------------------------------------+
| /campaign-plan/overview                  | #campaign-plan-overview                  | CampaignPlanOverviewController                               |
+------------------------------------------+------------------------------------------+--------------------------------------------------------------+
| /app/campaign-plan/overview.html         | /asset/less/campaign-plan/overview.less  | /app/campaign-plan/ CampaignPlanOverviewController.js        |
+------------------------------------------+------------------------------------------+--------------------------------------------------------------+
| /campaign-plan/detail                    | #campaign-plan-detail                    | CampaignPlanDetailController                                 |
+------------------------------------------+------------------------------------------+--------------------------------------------------------------+
| /app/campaign-plan/detail/main.html      | /asset/less/campaign-plan/detail.less    | /app/campaign-plan/detail/ CampaignPlanDetailController.js   |
+------------------------------------------+------------------------------------------+--------------------------------------------------------------+
| /media-plan                              | #media-plan                              | MediaPlanController                                          |
+------------------------------------------+------------------------------------------+--------------------------------------------------------------+
| /app/media-plan/main.html                | /asset/less/media-plan/main.less         | /app/media-plan/ MediaPlanController.js                      |
+------------------------------------------+------------------------------------------+--------------------------------------------------------------+
| /media-plan/...                          | #media-plan-...                          | ...                                                          |
+------------------------------------------+------------------------------------------+--------------------------------------------------------------+
| /...                                     | #...                                     | ...                                                          |
+------------------------------------------+------------------------------------------+--------------------------------------------------------------+


This sounds trivial and it actually is quite simple to implement - but what’s important is: this makes it trivial to find the files corresponding to some feature in the
application. Or to know what could be affected by a change in one of those files.

I hope you enjoyed this article and that it gives you a little insight in how we develop tools - even though this only scratches the surface of our everyday work.
