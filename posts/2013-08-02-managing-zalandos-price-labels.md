<!--
.. title: Managing Zalando's Price Labels
.. slug: managing-zalandos-price-labels
.. date: 2013-08-02 11:49:15
.. tags: draft,article,backend
.. author: ToDo
-->

Zalando has over 100 mio. different prices online in 14 countries for over 24
shops. We update between 50 000 to 3 mio. prices per day, upload on average
around 60 000 articles with new prices per week and have more than 50 sales
overall per year. Ever wonder how we manage all that? 

<!-- TEASER_END -->

## Our prices are clever

As there is so much to keep track of and manpower is hardly suffice,
we teach our prices to find their own way to the shop. We thrive when solving
problems. So we did not waste any effort in creating a simple yet flexible
environment to allow the fulfillment of some ingenious existing and
prospective ideas.

## There's a long road ahead...

...and in most cases it starts with a manual price upload. However, the uploaded price rarely reaches the
shop in the form it was uploaded. Below you'll find a fictive example for an
uploaded price of 43€.

[![Zalando's Price Upload Process (illustration by Kolja Wilcke)](/files/2013/07/Blogpost_lowres.jpg)](/files/2013/07/Blogpost_lowres.jpg)

_This is an abstracted and simplified model to give you a general idea. The details would exceed the
scope of this post._ 

As Zalando operates in several countries, the price also
needs to be converted to other currencies. To ensure that our shop only
contains nice looking prices, rounding and layout is done separately for each
country. This means that the path a price can take may differ for each
country. However, now the user feeding the price into the system to start off
with, no longer needs to worry about this anymore.

These users can now focus their time on deciding which strategy would be best in country A as
opposed to country B. As mentioned above, Zalando regularly reduces its prices
for sales in 14 different countries. In order for the sales to start right on
time, our prices can be set to start and stop at a certain point. This way no
one needs to sit in front of the screen 5am in the morning to punch in new
prices, and so the sale can end without anybody having to interfere. One more
cool feature to mention is the so called ‘price levels’.

A very simple example are the standard (black) prices and the promotional (red) prices. These two
levels have an inherent logic which describes that red prices (being our
promotional prices) always overwrite the black ones when they exist. There’s a
bunch of levels to choose from, each with their own behavioral properties. The
only challenge now, is to keep track of the various possibilities provided by
these levels.

## Nurturing a child

The tech world has come a long way over
the past 5 years. We always strive to take part in that growth, and this has
an effect on everything we do. Alongside prices, we have also evolved as we
grew. A great system has been born, but you can bet that it already looks
different the moment you read this post ;) 

## Acknowledgement
The brains behind the pricing logic are of course from another department within Zalando.
They are occupied with this topic day in and day out. Our Zalando Technology
Teams 'merely' provide the clever tools for them to do their magic. As
techies, we are not the only nerds here and we love to learn new stuff!
Please note that some of these numbers are estimates and vary greatly
depending on the time period in question.

