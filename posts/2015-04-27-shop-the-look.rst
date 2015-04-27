.. title: Shop the Look
.. slug: shop-the-look
.. date: 2015/04/27 14:45:00
.. tags: shop, design-thinking
.. link:
.. description: Shop the Look allows you to easily locate and buy the individual components making up a look.
.. author: Erik Schünemann
.. type: text
.. image: shop-the-look-phase-4.jpg

Here's a common user experience for Zalando customers: *You're checking out a shirt on its product detail page. You notice the full-body model image, which features a complete look, and become completely distracted when you suddenly notice that the model is wearing the exact style of sneakers that you've been looking for! You can't identify the sneaker brand, so you try to use filters to find the correct style in our shop. After clicking through dozens of pages showcasing hundreds of sneaker styles -- unfortunately none of which is the one you're looking for -- you abandon your search. In the end, you've wasted lots of time and haven't bought the shirt, let alone the sneakers.*

.. TEASER_END

Good news: We've solved this problem for you with a new feature called Shop the Look. Available on the product detail pages (PDPs) of more than 30,000 individual Zalando items, Shop the Look allows you to easily locate and buy the individual components making up a "look."

Why We Created Shop the Look
============================

One of our team's guidelines is to always test whether there is a proven need for a new product before we begin developing it. Testing revealed that the need for Shop the Look was very clear and obvious. Zalando customers love to be inspired by the seemingly endless array of looks we offer, but they also want to be able to easily buy the items making up these looks. As our Customer Care agents often tell us, Zalando users regularly call our support hotline asking how they can purchase items from individual looks they like.

Testing Underlying Assumptions
==============================

Several months before the first components of Shop the Look went live to our +14 million users, our product team used elements of the `Design Thinking`_ methodology and `Lean UX`_ to create two detailed click-dummies of the feature. We then invited several Zalando users to try it out in our in-house UserLab. They were all very, very excited about Shop the Look. "When is this cool thing gonna be live?" several users asked us.

The layouts of our two click dummies were very different from each other, although one was quite close to our final Shop the Look product. The underlying feature ideas and assumptions that we tested were the same for both:

1. **If an original article in a "look" is sold-out, we need to offer our users some similar alternatives.**

Few things are more frustrating for Zalando users than falling in love with an item, discovering that it's sold out, and not being able to purchase it. We've learned, however, that users rarely fall in love with an item's particular brand or price -- rather, they're drawn to its visual appearance. Therefore, customers are delighted when they are presented with visually similar alternatives. In many cases, they don't even care that the original article is sold-out.

2. **Users like to see accessories and other articles that complement and complete a look, even if the model is not wearing those exact items in the product detail page photo.**

When creating a look, our stylists try not to "over-decorate" the model with too many accessories. If the model is styled with a necklace, but the user wants a bracelet instead, we can use Shop the Look to provide these additional, complementary articles.

3. **Users want to see alternatives to the articles depicted in a "look" even when all the original articles are still available.**

This assumption proved correct in several scenarios:

* When the original article is still available, but not in the user's size. The user might find the correct size among the similar alternatives.
* When the user doesn't like the original article's particular brand, but likes or doesn't mind the brands of similar alternatives.
* When the user wants a more affordable alternative to the original article -- or, as so often happens, wants a higher-end version.

4. **Users want to know how many different looks they can achieve with a single article.**

Shop the Look makes this easy. Some users were so excited about this aspect of the feature that they couldn't stop checking out looks. We knew we had a hit on our hands!

5. **Users would like to gather different articles within Shop the Look, sift through them, and then add them all to their cart at once.**

Developing a complex feature that supports all of the above stated assumptions poses the risk of losing the user. With so many similar-looking articles, alternatives and even different looks to choose from, users might have trouble remembering which articles and looks s/he checked out already. With this in mind, we're monitoring our data to better understand, on a quantitative basis, how users are using the feature.

How We Designed and Tested the Access Point for Shop the Look
=============================================================

Here's how we tested the individual components and created an initial mockup:
To preserve the general structure of our product detail page and abide by our internal style/design guide, we've made Shop the Look accessible via a button fixed to the right of the feature. This is also where our other call-to-action buttons reside. Using our click dummies, we tested two different kinds of buttons. One version shows a mini-image of the whole "look":

.. image:: /images/shop-the-look-whole-look.jpg
   :alt: Button 1: Mini image of the whole look

The other version shows the individual items making up the look:

.. image:: /images/shop-the-look-individual-items.jpg
   :alt: Button2: Individual items making up the look

Our qualitative research highlighted the advantages of both versions:

* Version 1 states most clearly the kind of look customers can actually buy, and what, exactly, Shop the Look references; whereas
* Version 2 already uses this feature to indicates which items are available. It does not, however, point out that these items appear on the full-body model image.

Qualitative research showed that there is no clear tendency for one or the other version. Therefore, we've activated Version 1, which shows the full-body model image.

How We Designed and Tested Shop the Look's Layout and Usability
===============================================================

For the feature itself we created two different click dummies:
1. One used the whole screen width and pushed down the "currently viewed" product detail page after customers clicked the Shop the Look button. Female test-users preferred this version because its larger model images really showcase the looks.

.. image:: /images/shop-the-look-click-dummy-1.jpg
   :alt: Click dummy 1

2. The other handled the whole feature within one modal window upon a click of the Shop the Look button. We noticed that this version increases complexity by using less space and cluttering the feature's different functions.

.. image:: /images/shop-the-look-click-dummy-2.jpg
   :alt: Click dummy 2

Different Phases of Shop the Look's Development
===============================================

Following the minimum viable product (MVP) approach, we sliced Shop the Look into four development phases. Even though the final product is not yet finished, we have released it and added more functionality over time.

Shop the Look Phase I: Get the Look
-----------------------------------

* The user can shop by clicking the "Shop the Look" button on the PDP of each item
* If an item is not available, our recommendation engine proposes a similar item:

.. image:: /images/shop-the-look-phase-1.jpg
   :alt: Shop the Look phase 1

Shop the Look Phase II: Recommend Complementary Items
-----------------------------------------------------

* When a look features fewer than eight items, the recommendation engine suggests complementary items:

.. image:: /images/shop-the-look-phase-2.jpg
   :alt: Shop the Look phase 2

Shop the Look Phase III: Recommend Similar Items
------------------------------------------------

* The recommender suggests four similar, alternative items for each original and complementary item
* This feature went live in late 2014

.. image:: /images/shop-the-look-phase-3.jpg
   :alt: Shop the Look phase 3

Shop the Look Phase IV: Get Other Looks
---------------------------------------

.. image:: /images/shop-the-look-phase-4.jpg
   :alt: Shop the Look phase 4

* This feature relates to the proven assumption that users want to see an article in more than one look/styling
* Users can now check up to six other looks in addition to the look that initially caught their attention
* We added this feature in late March 2015

What Is Next?
=============

Now that Shop the Look is live, we will try to understand how customers use it. At the moment it's only available on our product detail pages. Please try it! If you have ideas, suggestions or comments, please drop my development team and me a line through `shop.the.look@zalando.de`_.
Here are some articles that Shop the Look already works with:

Men's Looks:

* `edc by Esprit - Shirt`_
* `Brooklyn's Own by Rocawear - Denim jacket`_
* `BOSS Orange - Chinos`_

Women's Looks:

* `Wood Wood - Light jacket`_
* `edc by Esprit - Denim shorts`_
* `American Vintage - Basic T-shirt`_

.. _Design Thinking: http://en.wikipedia.org/wiki/Design_thinking
.. _Lean UX: http://www.jeffgothelf.com/blog/lean-ux-book/
.. _shop.the.look@zalando.de: mailto:shop.the.look@zalando.de
.. _edc by Esprit - Shirt: https://www.zalando.co.uk/edc-by-esprit-shirt-light-indigo-blue-ed122d092-k11.html
.. _Brooklyn's Own by Rocawear - Denim jacket: https://www.zalando.co.uk/brooklyn-s-own-by-rocawear-denim-jacket-black-denim-mid-grey-melange-bh622h002-q11.html
.. _BOSS Orange - Chinos: https://www.zalando.co.uk/boss-orange-chinos-black-bo122e00l-q11.html
.. _Wood Wood - Light jacket: https://www.zalando.co.uk/wood-wood-anais-light-jacket-dark-navy-wo421g004-k11.html
.. _edc by Esprit - Denim shorts: https://www.zalando.co.uk/edc-by-esprit-denim-shorts-bleached-blue-ed121n018-k12.html
.. _American Vintage - Basic T-shirt: https://www.zalando.co.uk/american-vintage-jacksonville-basic-t-shirt-am221d03y-c12.html

