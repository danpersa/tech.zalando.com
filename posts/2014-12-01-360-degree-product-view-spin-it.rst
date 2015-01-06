.. title: 360-degree product view - spin it!
.. slug: 360-degree-product-view-spin-it
.. date: 2014/12/01 10:00:00
.. tags: frontend,project-management,innovation
.. link:
.. description: This TechBlog post explains how 360-degree images are produced and the feature evolved at Zalando.
.. author: Erik Schünemann
.. type: text
.. image: 360-degree-product-1.jpg

Have you ever taken a look at the shoe images in our Zalando Shop? You can see many views of the shoe and even get a detailed view of its interior. However, they are still just plain images showing the shoe from six different perspectives. To ensure that the customer can see the shoe from all horizontal angles, we developed the 360-degree feature. When the user tries this feature, he or she can see the shoe from all angles by dragging and dropping it. This is an interactive feature that both engages and delights the customer. This takes us another step closer to our goal of achieving the best online product presentation.

.. TEASER_END

**Production & Processing**

But let’s start from the beginning and hear from to Katharina - Product Owner in our Technology Backend Team Production:
 
The 360-degree images are created by the Zalando Content Creation teams. They are photographed in a Packshot photo box, which was especially designed for 360-degree-images. This photo box works quite simple: Open the box, position the shoe precisely in the middle of a rotating plate, close the door, put a camera in front of the hole in this door and press the start button. The plate then starts turning and on every 12° angle a photo is taken automatically. This results in 30 raw images.

Those images are then retouched by a designer using Photoshop, in order to make small corrections like adapting the color of the images to more closely resemble the physical article. Afterwards, the 30 images are uploaded into Zalando’s Content and Media Tool (CoMeT), which was developed by the Backend Team Production. CoMeT is the tool that enriches a basic article with all the information that is needed to display it in the shop. For example, you can upload descriptions, attributes, images, 360-degree images and style images. After uploading 30 individual images, CoMeT internally combines them into one large image, a so called “sprite”, which is then used to generate a preview of the rotating 360-degree image as it will appear in the shop.

.. image:: /images/360-degree-product-2.jpg
.. image:: /images/360-degree-product-3.jpg

To ensure the quality of the 360-degree image and to check if the article displayed here is the same as shown on the still images, a quality control step takes place. An employee of the Quality Control Team in the Content Creation department uses a separate “control” screen to ensure that everything is correct and arranges a reshoot when necessary. This control screen shows both the preview image and the first image of the rotating 360-degree image.

.. image:: /images/360-degree-product-4.jpg

If everything is correct, the 360-degree image sprite is sent to the Catalog Service, Zalando’s technical center for all article information, which is owned by the Backend Article Team. From there it continues its journey to the Shop.

**Shop Integration**

After the preconditions for implementing the 360-degree feature in the shop are prepared, my role as the shop product manager for that feature actually starts. 

My task is to find the best way to integrate the feature so that it is:

* Consistent with the current look and feel of the page in which it is embedded 
* Located where the user would expect it
* Easy for the user to understand 
* Enjoyable for the user to use and explore
* An added value for our business

Throughout the whole product development process, I kept the Minimum Viable Product (MVP) approach in mind. In short, this means: Start out with a product that has the lowest possible complexity but still offers an added value to the customer and improve the feature as we go.

First, I considered where this feature could be integrated. Every article has its own product detail page on which the user may buy the article. Clearly, this 360-degree feature conveys further product information and engages the user with a specific product and therefore must be located on the product detail page. Next, I scribbled and brainstormed by myself to consider how this feature and its integration on the product detail page should look like. The first person I approached for the integration of this new feature was our UX Designer. He proposed a space on the product detail page to integrate the feature and also some functionality. Furthermore, he made sure that the design of the feature matched our style guide.

This concept of the feature was then tested in our UserLab to make sure that the user understands the feature and enjoys using it. After user testing, the first version of the feature was implemented and released:

.. image:: /images/360-degree-product-5.jpg

The button to open and close the feature is very visible and it was easy for the user to notice the button and thereby this feature. However, the button destructs the nice, compact area of the main image and the thumbnails below.

**Improvement & Adaptation**

We did more user testing in our lab and studied the data that reflects how users actually use this feature. We noticed that users liked this feature but it still had room for improvement. The integration of the feature for example did not look appealing and users wanted to see the feature bigger than just in the product detail page’s image box. So following the MVP approach, we put more effort into this feature to bring even more added value to the customer. This is how we came up with version 2.0: 

.. image:: /images/360-degree-product-6.jpg

To give the user a full impression of the shoe at a glance, the feature starts immediately after the user opens the product detail page of the shoe. The shoe spins around once and a 360-degree-icon is placed in the top left of the image frame to make sure the user understands what to do with this feature.Consequently, the 360-degree button between the thumbnails and main image is no longer necessary and therefore was moved to the first thumbnail. Also, now the visually pleasing compact area of the main image and image thumbnails has been retained.
When the user hovers or clicks another product image and goes back to the 360-degree thumbnail, the shoe turns around once again. In this way, we make sure that even when the customer does not understand that he or she can turn the shoe by dragging it, he can still keep switching from thumbnail to thumbnail to turn the shoe again.

Because the shoe must fit horizontally in the vertically-aligned main image box, the shoe within the 360-degree feature may look a bit small to the customer. But by clicking the zoom icon, the user can open the image in an overlay which allows the user to enjoy the fun of this feature in a larger size.

.. image:: /images/360-degree-product-7.jpg

**Next Steps**

The 360-degree feature is perfect for mobile devices because the shoe can be turned by just a swipe of a finger. That is why it is currently being integrated in our mobile site as well.

.. image:: /images/360-degree-product-8.jpg

Since April 1, we have added about 10,000 shoes with a 360-degree view to our shop. Now that version 2.0 is live, we are considering how to improve the feature even further. A potential next step could be the offering of this feature for other products, such as bags and purses in order to provide our customers with the best online product presentation.

Examples:

| `Tiger of Sweden Casual lace-ups <http://www.zalando.co.uk/tiger-of-sweden-donald-11-casual-lace-ups-grey-ti512a010-c11.html>`_.
| 
| `Converse Chuck Taylor Trainers <http://www.zalando.co.uk/converse-all-star-ox-trainers-beige-co4-uzw-0009-99.html>`_.
| 
| `Nike Performance Football boots <http://www.zalando.co.uk/nike-performance-mercurial-victory-v-fg-football-boots-pink-n1242a0nm-j11.html>`_.
| 
| `Anna Field Ankle boots <http://www.zalando.co.uk/anna-field-ankle-boots-black-an611n01w-q11.html>`_.
| 
