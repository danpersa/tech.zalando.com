.. title: Where is my order?
.. slug: where-is-my-order
.. date: 2014/07/10 10:21:29
.. tags: feature, frontend, user-account
.. link:
.. description: “Where is my order?” is the most important question for our customers once they ordered at Zalando. With our new feature we are able to answer that question in the most elegant and comfortable way possible.
.. author: Mikhail Ostapenko
.. type: text
.. image: zalando-order-tracking.png

Well, I assume the most important question for every customer after a successful purchase at Zalando is “Where is my order?”
With our new feature we are able to answer that question in the most elegant and comfortable way possible.

.. TEASER_END


.. image:: /images/order-tracking-iconbar.png
   :alt: Order-tracking Icon-bar


**What is it all about?**

In the past, the only available information after receiving the confirmation email was “Your order will be processed in our logistics center” and “It has been shipped”,
which is not really enough if you want to know any additional details about the current status of your order.
One may also wish to see a step by step progress of the order from start to (I guess you know our slogan) the screaming moment of happiness.
Of course it was always possible to go to the delivery provider tracking page to view the progress once it was handed over to them,
however that took the customer away from Zalando, as they needed to visit an external site.

Here is the old layout of order tracking view (Please consider all screenshots are in German due to our incremental
approach to roll out big features at zalando.de first):


.. image:: /images/order-tracking-overview-old.jpg
   :alt: Order-tracking Overview-old


The future of order tracking is now upon us: Every person in Germany can easily follow their orders step by step right in the customer account without the need to go to any external page.
Our goal was to be more transparent and to provide all the relevant information regarding the whole order process in one place so that our customers may quickly obtain a crystal-clear view on what is happening right now and what will come in due time.
We will not only display events from our logistics centers, but all the parcel status updates from DHL, and even payment method information.

**How did we manage it?**

It was a huge project here at Zalando and many different teams across the whole company were involved in it: Frontend,
Backend, Business Intelligence, Platform, Logistics, Graphic and Customer Proposition and Innovation.
Technical efficiency and clear communication were our top priorities in order manage this project with the least amount of effort.
Every week we had regular jour fixes with product management members which were responsible for feature implementation in their teams and every second week a larger meeting with all team members involved.
This constant feedback and communication helped to ensure everything was on track and allowed us to solve any problems quickly and efficiently.
We also utilized the milestone project plan, which was shared in a Google Doc so everyone could take a look at it and quickly adjust it accordingly.

It was important to have one main responsible person for coordination and communication between all the teams.
In our case it was project manager who has dealt with the general project plan and fulfillment of it.
As product manager, I was in charge of the release cycles within my team and the technical updates with support from other project members.

For our initial setup we used MongoDB as a datastore, because of its ease of use for schemaless events and ability to index multiple fields.
However during the internal tests we switched to Cassandra as not only did its performance match our requirements,
but turned out to be very easy to setup and run when comparing it to MongoDB. We also used icon fonts for the first time in our shop,
which was a good decision to implement them due to performance and appearance issues on retina display devices. By the way,
almost all icons at Zalando are now icon fonts.

If I look back, for me as a product manager it was an absolute great experience to have learned so many new things how such projects should be managed.

**How does it look like?**

In the order overview you can already see what the current delivery status is and for any further details simply click on “Sendung verfolgen” (Engl. “Track my parcel”):


.. image:: /images/order-tracking-overview-new.jpg
   :alt: Order-tracking Neighbor-delivery


You will then see the modal window with all the important information for the selected order.
Here is an example where the parcel was successfully delivered to a neighbor Sandra Mustermann:


.. image:: /images/order-tracking-neighbor-delivery.jpg
   :alt: Order-tracking Neighbor-delivery


Prepayment, credit card, or PayPal payments display the payment icon after the “order placed” icon. However,
if you pay by invoice we display a useful message which contains the open amount and bank account information at the end
of the process so you may easily find all you need in order to make a payment:


.. image:: /images/order-tracking-payment-information.jpg
   :alt: Order-tracking Payment-information


**How did we test it?**

During the development phase we already knew without any testing that we cannot go live quickly with such a big feature
because of the potential customer impact. Therefore, we thought about how we could test it in a more efficient way and
concentrated on the following points:

* **User lab test.** It was very important for us to see if our new feature will be valuable and understandable for the customers or not. That’s why we tested the prototype face-to-face with some new employees in our own user lab. On the one hand we could gain some valuable feedback and as consequence improve some wordings so that everybody could better understand every single status we display. On the other hand, the testers could confirm our hypotheses regarding the progress bar flow meaning and icons which will be used.

* **Internal test.** After finishing the first fully working prototype, we activated the feature for 50 employees who wanted to test it and help us improve the feature. With their feedback we could see that everybody is able to understand the feature quite well and it is extremely helpful for them to see the whole order tracking information at once because of transparency and the amount of time saved. Additionally, the testers provided bug reports so we could identify important issues quickly in order to fix them in a timely manner. The next step was to enable the feature for all employees. After several weeks, we were able to see happy customers inside of our testing group. It was a great sign for us that we were finally ready to go live.

* **Test framework.** Another problem we encountered was the large number of scenarios which depend on different parcel statuses and payment methods. In order to test every use case we decided to come up with a framework with which even a non-developer should be able to write test cases without worrying about the implementation. This gave birth to an XML document structure of a test case, which could be easily copied over with minor changes to vary the test data. It was very helpful for our QA because they were then able to generate SQL statements, execute it on our test environment, and see how it looks in the frontend. For me and developer, it was also nice to know that everything worked as designed.

**What is next?**

The extended order tracking feature is available on our mobile site as well. Even better news is that Zalando iOS and
Android apps will receive new versions later this year which will include not only this order tracking feature, but
will also integrate push notifications for the most important status updates.


.. image:: /images/order-tracking-app-notification.jpg
   :alt: Order-tracking App-notification
   :width: 60%


We will see how customers respond to the new feature in the German shop and then implement some improvements where
required. Afterwards, we will integrate it into the remaining shops per country.

In conclusion, I hope you will enjoy the new way of order tracking inside your Zalando customer account.
Stay tuned for the future updates!