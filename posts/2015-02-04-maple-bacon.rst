.. title: Maple Bacon – Swift image downloads, caching and scaling
.. slug: maple-bacon
.. date: 2015/02/04 10:00:00
.. tags: ios, swift, hack-week, open-source
.. link:
.. description: MapleBacon is a delicious image download and caching library for iOS written in Swift
.. author: Jan Gorman
.. type: text
.. image: maple_bacon.png

Everybody’s favourite donut flavour is now available as an open source iOS library! During Hack-Week 3 the iOS team got together to release their first open source Swift library Maple Bacon – image downloading, caching and scaling done right.

.. TEASER_END

As you can imagine, a fashion app like `ours`_ downloads and displays a lot of images. Working in mobile poses numerous challenges. We obviously don't want to waste our customers' bandwidth or drain their batteries while at the same time maintaining a 60Hz refresh rate for a smooth scrolling and shopping experience.

Swift
=====

At last year's WWDC Apple introduced `Swift`_ to the world. And while Objective-C isn't going anywhere anytime soon, Swift does offer quite a few compelling reasons to start using it in your development now:

* Interoperability with Objective-C
* Type inference
* Immutable variables and types
* Closures (no tacked on blocks)
* Functional programming (filter, map, reduce)
* Static typing (ok… there's pros and cons here but the Optional system baked into Swift is pretty amazing)

To name just a few. Since we were already writing some code in Swift it was interesting to see how some of the new language paradigms would apply to a pure standalone library.

Hack-Week 3
===========

During the last Hack Week the team got together to rethink the way we're downloading and caching images in the app. Apart from doing it in Swift, we came up with a few more requirements:

* Easy to implement the 99% use-case
* Memory and disk caching and multiple storage regions
* Opt-in high quality image re-scaling

After a quick design session we got cracking.

Downloading
-----------

The most straight forward use-case is downloading images (with automatic caching). As is possible with Objective-C categories, Swift offers extensions to extend any class you want. And so, downloading an image is extremely straight forward:

.. code:: java

  import MapleBacon

  @IBOutlet weak var imageView: UIImageView!

  if let imageURL = NSURL(string: "something.jpg") {
      imageView.setImageWithURL(imageURL)
  }


Compared to Objective-C you'll notice straight away, that you use the if-let construct to unwrap the NSURL. This is due to Swift's `failable initializers`_ (force unwrapping optionals in Swift is a bit of a code smell). But compare this to Objective-C where you'd have to perform some sanity checks on the NSURL or other languages like Java that is statically typed but still forces you to perform null checks everywhere. Having Optionals at the core of the language is one of Swift's best features.

ImageManager
------------

For more control over the download (e.g. to opt in to error handling), you can also access the ImageManager class directly:

.. code:: java

  if let imageURL = NSURL(string: "…") {
      let manager = ImageManager.sharedManager

      manager.downloadImageAtURL(imageURL, completion: { (imageInstance, error) in
          …
      })
  }


The completion closure gives back an optional error value (note the inferred type information) and an ImageInstance which wraps the underlying UIImage as well as some additional state.

Cache
-----

Maple Bacon automatically caches all downloaded images, both in memory and on disk asynchronously. Per default images are cached for a week but you can pass in any NSTimeInterval you desire:

.. code:: java

  let maxAgeOneDay: NSTimeInterval = 60 * 60 * 24
  MapleBaconStorage.sharedStorage.maxAge = maxAgeOneDay


Apple encourages you to be a good citizen, so should you find your app coming under memory pressure, you can quickly purge any cached images from memory like so:

.. code:: java

  override func didReceiveMemoryWarning() {
      MapleBaconStorage.sharedStorage.clearMemoryStorage()
  }


The disk backed cache remains and once images are requested, they are added back to the memory cache from disk.

Scaling
-------

Per default, images will be scaled by the UIImageView automatically but you can also opt in to a higher quality way of scaling:

.. code:: java

  imageView.setImageWithURL(imageURL, cacheScaled: true)


Scaling that way uses `Core Graphics`_ so will take up some more resources but in general should also produce better results. And of course, it's done on a background thread as you'd expect.

Wrap up
=======

So there you have it: a modern library to cover all you iOS image related needs. It is available on `CocoaPods`_ and `github`_ with detailed installation instructions and a sample app to get you started. We hope you like it.

.. _ours: https://www.zalando.de/zalando-apps/
.. _Swift: https://developer.apple.com/swift/
.. _failable initializers: https://developer.apple.com/swift/blog/?id=17
.. _Core Graphics: https://developer.apple.com/library/ios/documentation/CoreGraphics/Reference/CoreGraphics_Framework/_index.html
.. _CocoaPods: http://cocoapods.org/?q=MapleBacon
.. _github: https://github.com/zalando/MapleBacon