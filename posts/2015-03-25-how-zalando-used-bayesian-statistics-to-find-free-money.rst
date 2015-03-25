.. title: How Zalando Used Bayesian Statistics to Find Free Money
.. slug: how-zalando-used-bayesian-statistics-to-find-free-money
.. date: 2015/03/25 11:00:00
.. tags: warehouse logistics, machine learning, baysian statistics, baysian modelling, gibbs sampling, statistics, graphical models, optimization, mathjax
.. link:
.. description: We decribe how we automatically estimate article weights from parcel weights and save a lot of money in the process.
.. author: Calvin Seward
.. second_author: Roland Vollgraf
.. third_author: Urs Bergmann
.. type: text
.. image: warehouse.png


Everyone likes free money--and when you’re running a huge business like Zalando, finding free money by making your systems more efficient can mean saving *millions* of Euros. That’s why I’m excited to tell you that the Zalando Data Intelligence team has recently found some free money. In this post, I’ll tell you how.

.. TEASER_END

THE GOAL
========

Until recently, the only way that Zalando’s warehouse workers were able to determine the weights of our hundreds of thousands of items was by weighing each item manually. As you can imagine, this was a labor-intensive, time-consuming and expensive process.

It recently occurred to us that we could greatly simplify our operations by replacing our manual weight estimation process with highly refined data from another, automatic process. Here’s where that free money for Zalando appears: By accurately inferring the individual item weights from the parcel weights, we save A LOT of Euros--and a lot of our workers’ time. 

THE FREE DATA
=============

The key here is that we already have *data for free* on the volume and weight of every parcel that leaves the Zalando warehouse.  After a parcel is packed but before it is given to our logistics partners (like DHL) for delivery to the customer, its volume and weight are automatically measured.  We just need to somehow get the individual article weights from this data. The figure below shows the weights and volumes of some parcels that were measured:

.. raw:: html

  <table style="border:0px solid white">
   <tr style="border:0px solid white"><td style="border:0px solid white">
    <object data="../images/weight-estimation/GMM_raw.svg" type="image/svg+xml" style="display: block; margin-left:auto; margin-right:auto">
     <img src="../images/weight-estimation/GMM_raw.jpg" />
    </object>
   </td></tr>
   <caption style="text-align:left; caption-side:bottom">
    <b>Figure 1: </b> 
    Weights and volumes of parcels sent from the Zalando warehouse, as measured by the volume scanner.
    The parcels with a low weight and highly varied volume are envelopes, and the voume of the envelope
    varies with the volume of the contents.
   </caption>
  </table>


THE NAIVE METHOD
================

One of the most basic methods we *could* use to infer item weights from parcel weights works like this: Say we send out three parcels with the inferred weights :math:`p_1, p_2, p_3`, and three items with the inferred weights :math:`w_1, w_2`, and :math:`w_3`. Since the warehouse software tracks which items were in which parcels, we get the following linear equation:

  .. math:: \begin{pmatrix}p_1 \\ p_2 \\ p_3\end{pmatrix} =  \begin{pmatrix} & & \\ & A & \\ & & \end{pmatrix} \begin{pmatrix}w_1 \\ w_2 \\ w_3\end{pmatrix}

Here, :math:`A\in\mathbb{N}^{3\times 3}` is a square matrix in which :math:`a_{ij}` is the number of times the :math:`j`-th item was in the :math:`i`-th parcel. We can now calculate the weights of the individual articles by using the formula:

  .. math:: \begin{pmatrix}w_1 \\ w_2 \\ w_3\end{pmatrix} = \begin{pmatrix} & & \\ & A^{-1} & \\ & & \end{pmatrix} \begin{pmatrix}p_1 \\ p_2 \\ p_3\end{pmatrix}
 
This strategy presents a few problems:

* The outbound scale is prone to measurement errors

* We don't always know the exact packaging type (the type of cardboard box) that the items were packed into

* We don't always know how much packing material, vouchers, and other stuff is included in the individual parcels

* Because there are far more parcels than items, and a lot of little unknowns and measurement errors along the way, the matrix :math:`A` doesn't have a true inverse

* There are some articles where we don't have enough information to accuracy estimate an article's weight.  Therefore our goal is to calculate not just point estimates but also *confidence intervals* so that we know how sure we can be about our estimate of an article's weight.

Because of Zalando’s massive size and speed of operations, we need a much cleaner, more accurate method. For this, our data intelligence team turned to Bayesian statistics. In our `next tech blog article <../posts/you-too-can-find-free-money-the-details-of-the-bayesian-model.html>`_ we’ll go into the mathematical details of the Baysian model we used.  If you want to see a cool example of statistical modeling in action, the next article is perfect for you. But this is the fluffy non-technical article, so we’ll go straight to showing you how awesome our weight estimation method is.

Results
=======

There are many different criteria for evaluating accuracy, so let's look at how our weight estimator performed compared to various evaluation criteria.

Measured vs. Estimated
----------------------

Many Zalando items have already been weighed manually, so a natural evaluation strategy would be to compare the measured weight of an article against its estimated weight:

.. raw:: html

  <table style="border:0px solid white">
   <tr style="border:0px solid white"><td style="border:0px solid white">
    <object data="../images/weight-estimation/estimatevsmeasured.svg" type="image/svg+xml" style="display: block; margin-left:auto; margin-right:auto">
     <img src="../images/weight-estimation/estimatevsmeasured.svg" />
    </object>
   </td></tr>
   <caption style="text-align:left; caption-side:bottom">
    <b>Figure 2: </b> 
    Estimated article weights vs. the weight obtained by weighing acutal article
   </caption>
  </table>
  
Pretty good, but there are still some errors. The next few sections explore why we believe that many of these errors came about from manual measuring, not from our weight estimator.

Net Parcel Weights
------------------

Another way to gain a stronger understanding of how our estimator performs is to subtract the weight of each parcel from the estimated weights of the items inside that parcel. Then we can see how the differences cluster around the true packaging weights.

Figure 3 shows the results of our manual process, in which we subtracted the measured items’ weights. This revealed two important things:

 * Many parcels have a negative weight once the item weights have been subtracted.  Clearly this can not be the case--there must be an error in the system somewhere.  

 * The net weights vary widely, and don't cluster nicely.
 
.. raw:: html

  <table style="border:0px solid white">
   <tr style="border:0px solid white"><td style="border:0px solid white">
    <object data="../images/weight-estimation/GMM_net.svg" type="image/svg+xml" style="display: block; margin-left:auto; margin-right:auto">
     <img src="../images/weight-estimation/GMM_net.svg" />
    </object>
   </td></tr>
   <caption style="text-align:left; caption-side:bottom">
    <b>Figure 3: </b> 
     The volumes and weights of parcels after we subtracted the weight of the items in the parcel, 
     where the item weights were otained via a manual weighing process.
   </caption>
  </table>
 
Instead of using the article weights obtained by the manual process, we used the article weights obtained by our weight estimator; this is illustrated by Figure 4. Almost all net parcel weights are greater than zero, and the parcels cluster into small balls.

.. raw:: html

  <table style="border:0px solid white">
   <tr style="border:0px solid white"><td style="border:0px solid white">
    <object data="../images/weight-estimation/GMM_final.svg" type="image/svg+xml" style="display: block; margin-left:auto; margin-right:auto">
     <img src="../images/weight-estimation/GMM_final.svg" />
    </object>
   </td></tr>
   <caption style="text-align:left; caption-side:bottom">
    <b>Figure 4: </b> 
     The volumes and weights of parcels after we subtracted the weight of the items in the parcel, 
     where the item weights were obtained via our weight estimator.  The orange lines represent
     where most of the mass of the clusters lie
   </caption>
  </table>

Confidence Intervals
--------------------

If you remember back, we didn't just want to produce estimates of article weights, but also wanted to generate so-called confidence intervals. A confidence interval is when we can say that an article weighs between 150 and 170 grams with a 90% probability. Our automated weight estimator delivers results that nicely fit the data.

In Figure 5, each blue dot represents an estimated article weight. The position of particular dots on the y-axis is the relative error defined as

.. math:: \frac{\text{measured article weight}}{\text{estimated article weight}}

If a dot is at 1 on the y-axis, the estimated and measured weights are the same. We order the dots by the size of their confidence intervals, with narrow confidence intervals on the left and wide confidence intervals on the right. The green lines are then the 5% and 95% confidence intervals (meaning 90% of dots should lie between the green lines). Many of the dots that lie far above the confidence intervals are articles that weigh more than the parcels they were weighed in: in other words, articles known to have inaccurately measured weights.

.. raw:: html

  <table style="border:0px solid white">
   <tr style="border:0px solid white"><td style="border:0px solid white">
    <object data="../images/weight-estimation/trumpet.svg" type="image/svg+xml" style="display: block; margin-left:auto; margin-right:auto">
     <img src="../images/weight-estimation/trumpet.svg" />
    </object>
   </td></tr>
   <caption style="text-align:left; caption-side:bottom">
    <b>Figure 5: </b> 
     Plot showing different relative errors in weight estimations and the confidence in the weight 
     estimations.  We see that for the vast majority of cases, the estimation lies between the confidence
     intervals.
   </caption>
  </table>
  

The Payoff
==========

Deriving our new measuring model and verifying that it works took some effort! But it was all worth it, because now we have:

 * Automatic weight estimations for each Zalando article, which saves workers time
 
 * A reliable way to know the accuracy of our estimations

And most importantly: our warehouse workers can now focus on getting your fashion to you as quickly as possible. That isn't just free money--that's priceless.

If you liked this post, be sure to read (and like) `the next article <../posts/you-too-can-find-free-money-the-details-of-the-bayesian-model.html>`_ with all the great mathematical details of our Bayesian model.
















