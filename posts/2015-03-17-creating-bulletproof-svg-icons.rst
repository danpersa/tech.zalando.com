.. title: Creating Bulletproof SVG Icons
.. slug: creating-bulletproof-svg-icons
.. date: 2015/03/17 08:00:00
.. tags: frontend
.. link:
.. description: A comparison of different spriting methods
.. author: Andrey Kuzmin
.. type: text
.. image: creating-bulletproof-svg-icons-superman.jpg


=============================================
Creating Bulletproof SVG Icons
=============================================

Any front-end developer working on a large website will eventually face the problem of how to prepare and effectively deliver icons to users. There are few ways to achieve this goal. At Zalando, we have been using CSS sprites and icon fonts. Neither solution is perfect, but both get the job done to a reasonable degree. This article will help you to evaluate existing solutions and ultimately decide which one will work best for you.

.. TEASER_END

What do we want from a spriting method?
=======================================

Before settling on a new method to deliver our icons, we have to address a few concerns – some related to the user-side, others related to our personal wishes as developers.

* **Performance:** The Zalando team always needs to consider network performance (especially in terms of payload and amount of requests) as well as rendering performance, which is particularly critical on mobile devices.
* **Browser support:** We want our icons to look crisp – not only on retina displays, but also on older browsers such as IE8 and Android 2.3. And we want them to be present even when JavaScript is disabled on the client.
* **Ease of use:** It should be simple to add a new icon, alter styles using CSS, and change icon color. Bottom-line: We want to ensure a high level of maintainability.

Which methods should we take into account?
==========================================

CSS Sprites
-----------

CSS sprites reduce the amount of requests by combining icons into a single image file. Sprites require some additional CSS code that shifts the background position of the image file according to the icon on display. You can use either PNG or SVG images to build CSS sprites, with some conditions:

1. Because PNG is a raster image format, you must provide an additional, larger copy for retina displays and a special media query to choose which one to display. The size of a raster image is usually greater than the same image in vector format.
2. SVG is a vector format that will solve issues with the retina screen, but keep in mind that its `rendering performance is worse than PNG <http://codepen.io/adrianosmond/pen/LCogn>`_. Even though they claim this issue no longer persists, we still see a drop in framerate (Chrome 40/OSX).

Icon font
---------

Icon font is a retina-proof method of building font files from a set of icons and then using the @font-face rule to load the icon front from CSS. This method is quite difficult to support because it relies on cumbersome build processes. Another drawback: You can’t have multi-colored icons in a font, but can only set one color using CSS. Scaling and aligning such icons can cause additional headaches, because you can only change the font size; changing width and height is not possible.

Lonely Planet Tech Lead Ian Feather has shared some great insights on the advantages of moving from an icon font to SVG in `this post <http://ianfeather.co.uk/ten-reasons-we-switched-from-an-icon-font-to-svg/>`_.

CSS with embedded data URIs
---------------------------

The third method that we’ll explore embeds images in CSS using base64 or url-encoded data URIs (see `Mozilla’s overview of data URIs here <https://developer.mozilla.org/en-US/docs/Web/HTTP/data_URIs>`_). By serving just one CSS file to the browser, this method reduces the number of requests. However, data `URIs are pretty slow <http://www.mobify.com/blog/data-uris-are-slow-on-mobile/>`_ and can drain all the power from your mobile device. And if you want to show the same icon in different colors, you’d need to provide a separate resource for each one.

**Сombining SVG icons with symbol tags**

The previous method combines multiple SVG icons into a single SVG file with <symbol> tags. You can then use these icons in HTML (more on this from `CSS-Tricks <https://css-tricks.com/svg-symbol-good-choice-icons/>`_). This method is quite efficient in terms of network performance, because you can load the combined SVG with an XMLHttpRequest. Or, if it’s small, you can simply inject it into the <body> tag such that no additional request is necessary. This method also enables you to `change the icons’ color <https://css-tricks.com/cascading-svg-fill-color/>`_ from CSS. The only downside to this method is browser support: SVGs do not work in Internet Explorer ≤ 8 and Android 2.3.

It’s a matter of time before each single browser will support SVGs, so with this in mind the Zalando team has adopted this method. For unsupported browsers, we propose a simple fallback, which we explain below.

What about the tooling support?
===============================

Luckily, Zalando had been using `gulp <https://github.com/gulpjs/gulp>`_ to build front-end assets. Because of this, I was able to integrate my open source plugin `gulp-svgstore <https://github.com/w0rm/gulp-svgstore>`_, which combines many SVG icons into one file and wraps them with <symbol> tags. It is easy to use this plugin in combination with other gulp plugins.

What about the fallback?
========================

Neither IE8 nor Android 2.3 supports SVG. If you don’t have to support these browsers, then feel free to skip this section. At Zalando, we do support these browsers, so after talking to one of our designers our team concluded that it’s fine to go with graceful degradation here.

There can be two ways for the fallback to take effect: When our JavaScript detects that the browser doesn’t support SVG, and when there is no JavaScript to begin with. In either case, we use `gulp-svgfallback <https://github.com/w0rm/gulp-svgfallback>`_ to generate a CSS sprite with a PNG image from the original SVG sources. We have to rely on a default color setting to fall back to, because we cannot use CSS to alter it.

If SVG is not supported, we inject a link to our fallback CSS into the head:

.. code-block:: javascript

  (function (d) {
    var el = d.createElement('div');
    el.innerHTML = '<svg/>';
    if (!el.firstChild || el.firstChild.namespaceURI !== 'http://www.w3.org/2000/svg') {
        el = d.createElement('link');
        el.rel = 'stylesheet';
        el.href = 'http://domain.com/fallback.css';
        d.getElementsByTagName('head')[0].appendChild(el);
    }
  })(document);

If JavaScript is unavailable for this check, the browser naturally falls back to a link that loads the same CSS from a <noscript> tag.

The bulletproof HTML code to include the icon as an Underscore template is:

.. code-block:: html

  <span class="icon icon-<%= spriteName %>">
      <svg width="<%= width %>" height="<%= height %>">
          <use xlink:href="#icon-<%= spriteName %>"></use>
      </svg>
  </span>

CSS code for the icon:

.. code-block:: css

  .icon {
      display: inline-block;
      vertical-align: middle;
  }
  .icon > svg {
      display: block;
      /* Allow color property to control fill color */
      fill: currentColor;
      /* Prevent SVG from being a target of the delegated event */
      pointer-events: none;
  }
  .no-js .icon > svg {
      /* Fallback CSS is served in <noscript> tag,
         so we have to hide SVG */
      display: none;
  }

.. image:: /images/creating-bulletproof-svg-icons-parachute.jpg
   :width: 40%
   :alt: PNG Fallback

Conclusion
==========

We compared a few different approaches for delivering icons to the user and decided to combine SVG Icons with symbol tags. This provided good performance and kept maintenance pretty simple.

Non-modern browsers gracefully degrade with CSS sprites using automatically-generated PNG images. If you are still using CSS sprites or icon fonts, we encourage you to try this method.

We open-sourced some code that we used to play around with the `various spriting methods <https://github.com/zalando/compare-sprite-methods>`_ and compare them to one another. Feel free to run it yourself!
