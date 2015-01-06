.. title: How we rolled out Mobile Apps internationally
.. slug: how-we-rolled-out-mobile-apps-internationally
.. date: 2014/08/13 10:14:00
.. tags: mobile, android, ios, iphone
.. author: Rushil Dave
.. image: how_we_roll_out_mobile_apps.jpg

Almost a year ago, we decided to launch our mobile apps internationally. We received great feedback from our mobile app users in Germany last year. Positive app reviews and a rapid increase in user engagement gave us the confidence to go forward with a complete international rollout, giving all our users the option to buy their favorite Zalando shoes and clothes on their smartphones and tablets.

.. TEASER_END


.. class:: text-center

| **Zalando offers a cross-device fashion experience**
| **to users in 15 countries across Europe.**
| 

Zalando operates in 15 European countries, each unique in terms of shopping needs and wants. That’s why our first challenge was to collect specific requirements from all these countries. Following that, we categorized these requirements in order to make changes to our internal Mobile API, in native mobile apps and on certain webviews embedded inside the apps. The Mobile API provided configurations required for country specific changes to hostnames, prices, currency, shipping countries, postal code positions, taxes etc. 

.. image:: /images/how_we_roll_out_mobile_apps_2.png
   :width: 100%


Another big challenge was the implementation. We needed to build our mobile apps in a way that they could deal with localization, location based shop detection and adapting to internal API configuration as mentioned above. We planned tasks collaboratively and started working on it. Both Android and iOS platforms provided nice methods for localization. Furthermore, the development done on the Zalando backend side helped us to adapt our apps faster. 

.. class:: text-center

| **Android is a little more complex**
| **when it comes to device fragmentation.**
| 

We found a major issue, however, during the implementation phase with featured and curated content that we present on our apps using teaser images. Android device fragmentation became a complex issue as we had to cover four different densities (mdpi, hdpi, xhdpi and xxhdpi) for these images. The tooling team supported us by implementing a very useful teaser uploading tool in record time. The uploading tool helped the merchandising team to upload more than 1000 teasers both quickly and efficiently. This kind of collaboration would never have been possible without the amazing team spirit at Zalando. 

The next task was to translate labels and pages inside Android and iOS apps into 12 different languages (for the 15 European countries that Zalando supports). Country management teams took action immediately, demonstrating their skills to manage keyword translations as well as optimize usability through those keywords. Country specific testing rounds began with each region coming and sitting together with developers to help them resolve functional as well as user interface related issues. Along with this, the search engine optimization team started working on optimizing app store descriptions for all 12 languages along with preparing screenshots to be uploaded as part of the app store localization. 

.. image:: /images/how_we_roll_out_mobile_apps_3.png
   :width: 100%
   

Finally, the Android app was ready and staged rollout began. We started with German speaking countries (Austria & Switzerland) followed by the Western, Southern, Eastern and Northern European countries. This was followed by the iOS app rollout with similar stages. Users already started noticing the Zalando app in relevant app stores and organic app installations began smoothly. In Switzerland, both the apps reached the “Numero Uno” spot in the shopping category within a week after rollout, and they still remain unbeaten. Other countries like Austria, Italy, Netherlands and Belgium saw huge growth in Zalando app users, and they continue to grow. We are currently working on making our windows phone app international so that our windows mobile users can also enjoy the Zalando shopping experience.

.. class:: text-center

| **A good way to internationalize is to rollout apps serially,**
| **enabling countries one-by-one and keeping an eye on user feedback.**
| 

Of course, we faced some challenges and bugs during the rollout phase but we fixed those issues with firefighting mode. One issue was related to automatically geo-locating users to give them the correct country and language combination to ease the localized shopping experience. The implementation is different in both iOS and Android apps. In Android apps, we locate users with the Telephony Manager interface methods to set the correct Zalando shop. To set the language of the app, we detect the user’s language locale and we set it as app language, if we support it. On iOS, we have one to one mapping with country and language. Setting up the correct country in our iOS app is done by detecting the user’s country locale. 

.. image:: /images/how_we_roll_out_mobile_apps_4.png
   :width: 100%


After the successful rollout in all the countries Zalando is present, we organised a nice party in our sky lounge with beer, sandwiches and music to celebrate the occasion. In my opinion, this project displayed true Zalando spirit, which has it all: a problem-solving mindset, dynamism, team effort, professionalism and the drive to solve new technical challenges. All in all, it was a great effort from all teams involved and together we achieved an important milestone.
