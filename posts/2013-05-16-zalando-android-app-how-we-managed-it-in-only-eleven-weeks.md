<!--
.. title: Zalando Android App – How we managed it in only eleven weeks
.. slug: zalando-android-app-how-we-managed-it-in-only-eleven-weeks
.. date: 2013-05-16 10:00:26
.. tags: android,mobile
.. author: Carsten Ernst
.. image: android-logo_teaser.png
-->

Android is the most widely used mobile operating system in
the world. So we, at Zalando, wanted to offer our Android users, a Zalando app
to provide them the best shopping experience. I would like to give you a peek
into the work of the Mobile App Team - taking care of bringing you Zalando's
mobile apps - and more importantly how we managed to successfully complete the
Android App Project in only eleven weeks.

<!-- TEASER_END -->

## Small But Smart Team
Our team consisted of three developers and one development teamlead, three QA managers,
and one product manager. It was a small but smart group of young people, who
wanted to get things moving. In the meantime, we made our team stronger with
the addition of one developer as well as one product manager and as we would
like to expand the team further, we are constantly seeking for talented people
to [join us](http://www.zalando.de/karriere/unternehmensbereiche/it/). It is
our proclaimed objective that basically all developers and QA colleagues know
all about the three main components we are working on: The mobile API and the
mobile apps for iOS and Android.

Before we were ready to start, we needed to
define all required features. Here we decided that the first version should
have exactly the same functionality as the current iPhone app. This was also
practical for development reasons, so that in future, features can be
impemented in all components at the same time, in mobile apps and mobile API.
In addition much of the look and feel of the iPhone app could be borrowed
whilst taking into account Android's specific characteristics such as the
inclusion of the typical hardware back button.

## Planning Kick-off - App "Dismantling", Consecutive Milestones, Time Commitment, Specifications
In our kick-off meeting we decided upon which app components were required. To
even be able to shop with an app, a certain number of basic so-called
"activites" need to be developed. These include basic essentials such as
category browsing, search, filters, catalog view, product detail page, a
shopping cart and the checkout. In addition, extra features such as a barcode
scanner, the wish list, and the Styleshaker needed to be implemented, as well
as the integration of the News & Styles Magazine and the Zalando Lounge
campaign overview.

After we identified the individual components, we wrote
them on a series of post-it notes and put them into a logical order, which was
followed by lengthy discussions. In the end we had a rough development
overview and could start with time estimation. Every one of us committed to
the plan to shipping this app after a ten weeks development phase (+ one week
bugfixing), before we finally got green light from our senior management. 

[![Zalando_Androids](/files/2013/05/project_postits1.jpg)](/files/2013/05/project_postits1.jpg)
The entire Project was divided into eight milestones and was
mapped afterwards onto [Jira](http://www.atlassian.com/software/jira/overview)
tickets where each individual feature was specified to the smallest of
details. In total the project was made up of 32 separate tickets. 

## Early Inclusion of Quality Assurance, The Hockeykit, And Our First Shopping Trip
[![Zalando_Android](/files/2013/05/Project_chart1.png)](/files/2013/05/Project_
chart1.png) As you can see in the project Gantt chart above, all these
milestones were built upon and complemented each other. In the first step, we
took care of the cookie handling and URL caching, and we always had an eye on
devoloping things as re-usable as possible, like a webview that we implemented
at several points in the app. We set ourselves the target to be able to shop
with the app after the fourth milestone. Even if everything was not perfect
yet we wanted to be able to pass this obstacle, and be able to involve our
colleagues from QA early so that they could become part of the development
process.

For the internal distribution of test versions, we chose
[HockeyKit](https://github.com/therealkerni/HockeyKit) as a foundation. As of
that moment, we could rely on receiving prompt feedback on possible bugs from
our colleagues. Now the QA managers could not only report on successful
development phases but also on possible bugs.   

## The Final Stretch - Optimization And Practical Tests
In the last project week all of the
requirements had been fulfilled, known bugs fixed, different code optimization
implemented, and loggings removed. Our app was crowd-tested using
[testCloud](https://www.thetestcloud.com/) and
[Testbirds](http://www.testbirds.com/). The result was markedly positive,
because no critical bugs were found. A few problems occurred on older Android
devices along with a couple of usability suggestions. After these were
eliminated and subsequently tested by the QA, we received a green light for
the market launch. Through an excellent team performance and due to the self-
scarificing spirit of each of us, we then submitted the Zalando Android app to
the Google Play Store and went out for a delicious meal, and a few drinks of
course ;)   

## To Wrap It Up - The Important Success Factors

  * compact and motivated team
  * a well-designed plan
  * daily status meetings
  * modularity and re-usabilty of components
  * early stage UI development
  * early QA involvement
  * Last but not least: An excellent team spirit

[![Zalando_Android](/files/2013/05/en_app_rgb_wo_45.png)](https://play.google.com/store/apps/details?id=de.zalando.mobile) 
The app is now available on the
[Google Play Store](https://play.google.com/store/apps/details?id=de.zalando.mobile) and 
[AndroidPit](http://www.androidpit.de/de/android/market/apps/app/de.zalando.mobile/Zalando-Mobil). 
Please feel free to download it to your Android phone to browse our company’s great 
fashion offer. We hope you enjoy it!

