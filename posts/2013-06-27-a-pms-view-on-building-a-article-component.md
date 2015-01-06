<!--
.. title: A PM's view on building a ZEOS Article component
.. slug: a-pms-view-on-building-a-article-component
.. date: 2013-06-27 10:09:27
.. tags: article,backend,development,erp-system,key-user,product-management,project-management,reporting
.. author: Artur Weber
.. image: articles_teaser.jpg
-->

Summer two years ago we made the
decision to conceive and develop our own management system for our core
processes, called ZEOS. These included the process from the supplier advice of
articles, population of our shops with new fashion highlights, to the
management of actual orders and more. With Zalando’s core goal of creating the
world’s best fashion experience for our customers, we wanted to help our
internal customers to improve their working environment as well as become
enthusiastic about using our tools! One of them is the Article Management Tool
used to create and change our article data.

<!-- TEASER_END -->

## Reasons were not that hard to find...

But why? It wasn’t just because we could! :) With Zalando’s immense growth, its expansion to 14 countries and distribution to various sales channels during the last few years, a [high performance and scalable platform](http://tech.zalando.com/platform/) was more than just necessary. Since the proprietary system that we used to manage our core processes with (the [ERP-System](http://en.wikipedia.org/wiki/Enterprise_resource_planning)), no longer corresponded to our goals any more, it was quite necessary to make the decision to build our own management system!

Some components of ZEOS were already complete and were making us and our customers very happy (even if they do not directly see it in the shop front end :) ). Other components only just went live a couple of weeks ago, making it possible to finally shut down the good old ERP-System! One component’s requirement was to build a completely new Article Creation Tool, which would be used to create and update article data, and to set-up a whole new back end for article data - which has now become something that our internal customers can no longer do without!

## How to make internal customers scream

Of course many decisions had to be made, and we and the process management people had very intense and productive discussions with all of the involved stakeholders, including the Category Management, the Content Management and the Shop Front End team during this concept phase. As you can imagine compiling all of the requirements and must-haves for a completely new article data structure as well as putting it together in an elaborate and functional concept plan is not that easy. However it formed the foundation for a successful project, and so the effort was worth it!

Still, even with such a foundation further steps had to be defined for the project, and the following were what actually made ours a great success: 

### 1. Focus on needed functionality
We at Zalando really like a challenge (our motto is: think big and act fast! :)), and since time was a constraint we concentrated on core features which were already there in the old system as well as new must-have features. Also, the implementation covered features that were required by the defined article model such as our 3-step article structure (based on colors and materials as well as sizes) or an inheritance function for several article attributes. 

### 2. Some further nice features are always welcome
However, putting some cherries on top is always a good thing to make your customers happy. So if the project plan allows you to do so (and it should), make at least some wishes come true. We did this by introducing cool filtering or copy functions when creating or updating article data, which made the process a lot faster. 

### 3. Don't forget the long run
When planning the technical implementation we also tried to keep the future in mind. This wasn’t just about keeping a wish list, which would come as a set of features after the project. The back end had to be prepared for further component integration alongside the cool features based on requirements coming from other departments. 

### 4. Get clear about the tasks and the needed time
One key factor was to define the complexity and the required dependencies for the various tasks. So depending on the requirements we wanted to rank all tasks by complexity ranking from 1 (easy) to 5 (difficult). After this step we defined the dependencies, which gave us a high-level overview on what and when everything had to be implemented. Using this information modelling a project chart, a [Gantt chart](http://en.wikipedia.org/wiki/Gantt_chart) for example can be quickly made. The only thing here one needs to think about is how long a task will actually take. Important, in order to determine the project length at all, it is very important to consider team setup and  individual expertise. 

[![Zalando Article Project: Rough project chart, displaying the timeline of each role](/files/2013/06/High-Level-Project-Chart.png)](/files/2013/06/High-Level-Project-Chart.png)

 [![Zalando Article Project: JIRA analysis for project process](/files/2013/06/JIRA_Analysis.png)](/files/2013/06/JIRA_Analysis.png)

### 5. Keep an eye on project process and report regularly
Having a clear project plan is essential for keeping track of what is done and what comes next, and in turn makes it possible to work out the impact a delay in the delivery of a feature may have. So in order to keep everyone in touch with the project, especially our senior management, a short weekly meeting is the right place to show everyone where the project stands, and present the overall process, problems and next steps. 

### 6. Prepare the migration scenario properly
Another important thing is planning the data migration properly. Migrating sensitive data is always a big deal. Therefore having the relevant stakeholders in order to define the rules is always a good idea, since data has to look the same as before the Go-Live. Of course conducting several test-iterations always increases the probability of success! 

### 7. Involve your customers since the beginning
Even with a reasonable concept, knowing what to implement, having a detailed plan and project process management still does not guarantee the acceptance of your customers. So we did something quite simple which had a strong effect: [![Zalando Article Project: Mockup Article Management Tool](/files/2013/06/Mockup-Create-new-Article.png)](/files/2013/06/Mockup-Create-new-Article.png) One of our numerous mockups for the new ZEOS Article Management Tool When the  front end design had been completed, we showed it to our customers, and had a discussion about structure, usability and functionality. By doing this they had the possibility of actively influencing the front-end development and decide upon any necessary changes. We could then use this feedback to improve implementation, this was our first step to increase user acceptance. The second step was to introduce key-user tests for 3 weeks. This had been part of the project plan since the start, in order to create user anticipation. Specific users were chosen (up to 30) and were given the chance to challenge the whole application. This helped us identify bugs within the application itself, and at the same time helped test the data quality (compare point 6) early enough in order to correct them before the Go-Live. It also made it possible to spread the word within every department that the new tool was quite nice ;) 

Having the possibility to make our users curious about their new cool tool and
then actually fulfill their expectations was a great experience. Getting in
touch with them and actually seeing the world from their perspective has been
a lot of fun. Of course, we also learned a lot for future projects. Overall,
it was a win-win situation!

## And in the end...

[![Zalando Article Project: Happy key-user](/files/2013/06/happy-Key-User.png)](/files/2013/06/happy-Key-User.png)
Björn, one of our happy key-users the Teams of Category
Management, Buyers and Merchandisers gave a big "Welcome ZEOS" party for us,
where we had a lot of fun and actually received new requirements for further
nice features! ;)

On a final note, one can say that getting customers onboard
on the release process early brings out benefits for the whole project, making
it possible to go live with a system that is really accepted by them, making
all our lives easier :)

