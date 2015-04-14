.. title: Mobile Engineering at Zalando
.. slug: mobile-engineering-at-zalando
.. date: 2015/04/14 10:00:00
.. tags: ios, mobile, jenkins
.. link:
.. description: Mobile engineering at Zalando
.. author: Jan Gorman
.. type: text
.. image: mobile_engineering.jpg

Every year more and more of Zalando’s total traffic comes from mobile. Since releasing our first app in 2012, we've developed `award-winning`_ mobile platforms that deliver first-class shopping experiences to our +14 million customers across Europe. This post reveals insights into Zalando’s development approach to `mobile apps`_ – focusing on iOS for now. We’ll tell you about our Android operations in a separate post. 

.. TEASER_END

CocoaPods and Modules
=====================

Like many iOS shops, we use `CocoaPods`_ to manage all of our dependencies, both internal and external. Before adopting CocoaPods for private pods too, reusable modules of code were all part of the main application, but we have since pulled most of them out into local pods. Keeping modules as truly separate units of code forces greater discipline on the developers, requiring them to think more deeply about dependencies. Another neat side effect: less hassle merging, because dev teams end up with fewer (or no) conflicts in Xcode’s project file. 

A cool feature of CocoaPods is that it isn't just bound to Git or GitHub, but also allows you to define pods with a local path, e.g.:

.. code:: ruby

  pod 'TeaserLayout', :path => 'Modules/TeaserLayout'
  
For now the Zalando team has opted to keep all local pods inside of the application repository so that we don't have to check out 20 different sub-projects just to work on them.

Release Trains
==============

Zalando Mobile has worked in an agile way since we launched our first app. In late 2014, we slightly tightened up our development process to adopt fixed, four-week release trains. We now work in weekly sprints that we kick off every Monday with a planning meeting; we also have a regular release schedule that we're always working toward. This shortened cycle helps us to manage the scope of a release much better than our old process, during which release intervals were slightly longer. The four-week cycle gives us three weeks to work on new features, and one week of bug fixing. We usually don’t need every developer for the bug-fixing phase, so we can spend the remaining time working on new features going into the :code:`development` branch. More on branching to follow.

Process
=======

As a reflection of our commitment to engineer autonomy, Zalando’s mobile developers are free to work on whichever features they choose. If a new feature is particularly complex, we hold a quick technical design session before setting to work on developing it. One developer will take the lead, do some extra work to prepare for the session, and propose a solution to the rest of the team. The developers then discuss the idea and explore alternatives. This usually only takes around 20 to 30 minutes, and it's well worth the extra effort. We've had some great success with this approach: It leads to nicer designs and ensures everyone is on the same page. This better knowledge spread also helps a lot with ongoing feature maintenance.

Every feature we merge goes through code review. Our central repository ensures that it's impossible to merge code that no one on the team has reviewed. Usually two developers review code, but sometimes others will join in--especially if it's in their language of expertise, or the pull request is particularly large. We prefer to keep pull requests small, though, and if a feature takes a long time to develop then we’ll encourage our engineers to open several smaller requests. `thoughtbot`_ has a nice guide on code reviewing.

Continuous Delivery
===================

One of our goals is to automate (almost) everything. We set up continuous integration pretty much from the start, and over time our build script has grown quite powerful. We follow the `git flow`_ model of branching, which means that:

* new features are created off :code:`develop` branch, then merged back in
* a week before we plan to release, we pull a :code:`release` branch. Only bug fixes go into this branch
* After submitting the app, we merge the :code:`release` branch back into :code:`develop` and :code:`master`, where it's tagged for future reference.

This model ensures that all bug fixes done in the :code:`release` branch always make it back into the :code:`develop` branch. A stable :code:`master` allows us to pull a :code:`hotfix` (which we merge back into all other branches) should anything unexpected happen after rollout.

For all of these different branches, we trigger separate kinds of builds on a Mac Mini running `Jenkins`_ with a custom Ruby-build script. Every :code:`feature` branch triggers our unit test suite. And because of the way we’ve configured our central repository, there must be at least one successful Jenkins build before the feature can be merged back into the :code:`develop` branch. A change to that branch, in turn, triggers A. a full build that is automatically deployed to `HockeyApp`_; and B. a separate build that runs a bunch of `KIF`_ acceptance tests. 

The goal is to always have a deployable state of the app ready to go. You don't really want to rely on having an engineer, a live chicken and a voodoo doll at hand every time you want to publish to the App Store. Releasing should be drama-free, and everyone on the team should be able to do it. Keep everything you need to build, deploy and test in version control!

Part of the continuous delivery mantra is: If it hurts, do it more often. This sounds a bit strange, but it’s a strong incentive to automate manual steps much more quickly. 

Take, for example, the introduction of canary builds. As mentioned above, we use CocoaPods extensively. But upgrading external dependencies was always a manual step that required one of us to run :code:`pod outdated`, check for anything new, then update the pods. Because this results in a checkin, it triggers all the Jenkins jobs mentioned above. So why not automate that, too?:

.. code:: ruby

  def build_canary
    updates = $x{pod outdated}
      .lines("\n")
      .select { |line| line.start_with?('-') }
    return if updates.empty?
    %x{pod update}
    %x{xctool test}
    # Run any other steps, send an email/ping us on Slack
  end

A quick review of the updated pods still makes sense, but this method is much quicker than the old way.

Tools
=====

For our final section, let’s take a look at this random list of additional tools we use:

Instruments
-----------

Apple provides us with great tools for `instrumenting code`_. Learn to use them. The most common ones to begin with are the Time Profiler, Allocations and Leaks.

xctool
------

We switched from :code:`xcodebuild` over to `xctool`_ quite recently, and it has already helped us to greatly reduce the complexity of our build script. In addition to being easier to use, one of its coolest features is support for multiple `reporters`_. We have it set up to report **pretty** (which is also stored as the final build log); **junit**, which Jenkins is able to understand; and **json-stream**, which our devs can subscribe to any time a build is kicked off.

gcovr
-----

`gcovr`_ allows us to transform the gcov output generated by Xcode into something that Jenkins can understand and render into a pretty graph. To avoid messing up your numbers, you'll want to exclude external pods and the Apple frameworks:

.. code:: bash

  /usr/local/bin/gcovr \
    --exclude='(.*./Developer/SDKs/.*)|(.*Tests\.{m,swift})|(.*./Pods/.*)' \
    -x -r . > ./coverage.xml

New Relic
---------

We recently switched from `Crashlytics`_ to `New Relic`_ . Crashlytics is an amazing tool (and free), but the amount of additional insight that New Relic provides has to be seen to believed. You get detailed information on how long views take to render, how much time they spend talking to our API, and so much more.

Conclusion
------------

We hope you learned something from this. `Ping us via Twitter`_ if you have any comments or questions -- we love to hear from mobile devs at other companies.

.. _award-winning: http://www.internetworld.de/shop-award-2015-details-850468.html
.. _mobile apps: https://www.zalando.de/zalando-apps/
.. _CocoaPods: http://cocoapods.org
.. _git flow: http://nvie.com/posts/a-successful-git-branching-model/
.. _Jenkins: http://jenkins-ci.org
.. _HockeyApp: http://hockeyapp.net
.. _KIF: https://github.com/kif-framework/KIF
.. _xctool: https://github.com/facebook/xctool
.. _gcovr: http://gcovr.com
.. _Crashlytics: https://try.crashlytics.com/
.. _New Relic: http://newrelic.com
.. _thoughtbot: https://github.com/thoughtbot/guides/tree/master/code-review
.. _instrumenting code: https://developer.apple.com/library/mac/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/Introduction/Introduction.html
.. _reporters: https://github.com/facebook/xctool#reporters
.. _Ping us via Twitter: https://twitter.com/ZalandoTech