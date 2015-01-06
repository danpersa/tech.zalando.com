.. title: Show hidden navigation on-click without JavaScript
.. slug: hidden-navigation-onclick-without-javascript
.. date: 2014/05/20 10:21:29
.. tags: css
.. link:
.. description: How to build a hidden navigation and show it  on click without JavaScript and just using HTML and CSS
.. author: Sven Kunz
.. type: text
.. image: css3.png

We all have seen many of those famous “Hamburgers” in headers while surfing on pages with our beloved mobile devices. So what is it all about?

As we have been used to build web pages for larger screens we were not forced to face the problem of available space that much and if so, well, we just had to add an overlay navigation on hover to add more links to our navigation.

This still works fine for desktop screens and maybe it will always do. But what happens to mobile devices such as smartphones or tablets?

.. TEASER_END

Mostly there is no hover-event or mouseover on touch-devices. And there is probably not enough space to fit in all the navigation links to the screen, too.

The most common method is to hide the navigation and only show it to the user by touching an icon or wording. Nothing special so far, right? There are different ways to implement that and usually it is not worth thinking of different ways, it’s just so easy with JQuery and co.

But what about doing this without JavaScript? Is there any way to do so and if so, what will be the advantage?

So believe me, it is quite easy to get it done. You just need one more additional HTML element and two CSS selectors with six lines in total!

The explanation below will show you how:

#. First of all we are adding a ``<label>`` to our DOM. In our case we would like to add it to the ``<header>``. But it can be placed everywhere you need it.
#. We now add the element we want to be triggered by the ``<label>``. We go for the <nav> because we are building a hidden navigation.
#. Finally we add an ``<input>`` element to address the navigation. We are doing that by placing it as sibling element right before the ``<nav>``. We use type “checkbox” to set it checked and unchecked with our ``<label>``

.. code:: html

    <header>
        <label for=”menuTrigger”>Trigger</label>
    </header>

    <input id=”menuTrigger” type=”checkbox”>

    <nav>
        Your Navigation Content
    </nav>


Let's add some CSS to make it work:

#. We have to hide our navigation and of course the ``<input>`` element, we do not want to see.

#. To show the navigation by click on our ``<label>`` we add a ``display: block`` to the navigation if the <input> element will have the status ``:checked``. We can address the sibling everywhere in the DOM but this perhaps won't work in every Browser. So we placed the ``<input>`` right before the ``<nav>`` element.

.. code:: css

    nav,
    #menuTrigger {
        display: none;
    }

    #menuTrigger:checked + nav {
        display: block;
    }


**DEMO** on Fiddle: http://jsfiddle.net/GLORIEN/YuzqF/


So what happened here?
We take that state of the element to actually give the sibling element right behind a different style.
In this example from “``display: none``” to “``display: block``”.

And we do that by using the CSS3 pseudo-class selector :checked http://www.w3.org/wiki/CSS/Selectors/pseudo-classes/:checked


As we can see it is very easy, very fast and you don’t need any JavaScript for it at all. If you are fine with adding an additional ``<input>`` element than it could possibly be your next on-click menu.

As already mentioned, it won’t work in every Browser. So as the pseudo-class is part of CSS3 there is no support in IE8 and below. Browser support: http://www.quirksmode.org/css/selectors/#t60
I also had some issues related to the ~ selector for siblings in Android-browsers on HTC Devices. So make sure to always check your work properly.

