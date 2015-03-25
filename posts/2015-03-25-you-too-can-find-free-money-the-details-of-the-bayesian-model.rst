.. title: You Too Can Find Free Money: The Details of the Bayesian Model
.. slug: you-too-can-find-free-money-the-details-of-the-bayesian-model
.. date: 2015/03/25 10:00:00
.. tags: warehouse logistics, machine learning, baysian statistics, baysian modelling, gibbs sampling, statistics, graphical models, optimization, mathjax
.. link:
.. description: We decribe how we created a Bayesian model to automatically estimate article weights from parcel weights.
.. author: Calvin Seward
.. second_author: Roland Vollgraf
.. third_author: Urs Bergmann
.. type: text
.. image: weight-estimation/bayes_icon.png

In our `previous article <../posts/how-zalando-used-bayesian-statistics-to-find-free-money.html>`_, we described how the Zalando Data Intelligence team accurately infers individual item weights from the weights of parcels we send to our customers. But we didn’t share the secret sauce--the juicy details of building a Bayesian statistical model. In this article, we want to fill in these gaps and explain exactly how we constructed the model that got us such great results.

.. TEASER_END

In the spirit of `Baysian statistics <http://en.wikipedia.org/wiki/Bayesian_probability>`_, the Zalando team now looks for estimations of individual item weights that both explain the data and fit our preconceived beliefs (for example, the belief that errors that the scale makes are in a certain range, or that no article weighs less than 50g). We use statistical modeling to enforce these beliefs and assumptions. Let’s now explore some of these beliefs in greater detail--and with graphical models (see [Bishop]_ for an overview of graphical models).  

A Sneak Peek at Our Model
-------------------------

.. raw:: html

  <object data="../images/weight-estimation/model14.svg" type="image/svg+xml" style="float:left; margin-right:10px; margin-top:5px">
    <img src="../images/weight-estimation/model14.jpg" />
  </object>
  
Let’s take a quick look at what the finished model looks like. On the left is a graphical representation [Bishop]_ of the final model, in which we use the Greek letters :math:`\alpha, \beta, \mu` and :math:`\sigma` to represent priors (how we believe the system should behave) and Latin letters like :math:`X, Z, V` and :math:`k` to represent concrete values (for example, the weight of a parcel or item, or the volume of a parcel). The arrows represent dependencies: For example, the weight of a parcel :math:`Z_{j}` depends on the weights of the individual items in that parcel :math:`X_{1j},\dots,X_{L_jj}`.

Now let’s explore where exactly each element in the graphical model comes from, and the exact relationship between dependent elements.

Parcel Weight and Volume
------------------------

.. raw:: html 
  
  <object data="../images/weight-estimation/model1.svg" type="image/svg+xml" style="float:left; margin-right:10px; margin-top:5px">
    <img src="../images/weight-estimation/model1.jpg" />
  </object>

From the volume scanner we observe the parcel weights :math:`Z_j` and parcel volumes :math:`V_j` of :math:`M` parcels. Because of measurement errors, these are not the true weights and volumes of the parcels--but we can model the errors later on in the process.

Parcel Item Weights
-------------------

.. raw:: html 
  
  <object data="../images/weight-estimation/model2.svg" type="image/svg+xml" style="float:left; margin-right:10px; margin-top:5px">
    <img src="../images/weight-estimation/model2.jpg" />
  </object>
  
In this step, we model the assumption that the weight of a parcel :math:`Z_j`, given the weights of the items contained in that parcel :math:`X_{1j},\dots,X_{L_jj}`, is equal to the sum of the weights of the individual items in that parcel plus a Gaussian error. We use the term "parcel item" to distinguish individual items in a parcel from an "article," which is--in Zalando speak--a SKU. Note that the Gaussian error :math:`\varepsilon_j` doesn't require a zero mean; in this way, we can model the weight of packing material with the mean. 

The mean of :math:`\varepsilon_j` then models the weight of the shipping box and packing material for a particular parcel, and the variance of :math:`\varepsilon_j` accounts for how much unexplained noise we believe to be in the system: scale measurement errors, unknown changes in packing material, etc. (I’ll model the mean and variance of :math:`\varepsilon_j` in the next section.) Putting this into a formula, we get:

  .. math:: Z_j \mid X_{1j},\dots,X_{L_jj} = \sum_{l=1}^{L_j} X_{lj} + \varepsilon_j

Prior Information on Parcel Weights
-----------------------------------

.. raw:: html
  
  <object data="../images/weight-estimation/model3.svg" type="image/svg+xml" style="float:left; margin-right:10px; margin-top:5px">
    <img src="../images/weight-estimation/model3.jpg" />
  </object>
  
Zalando uses :math:`K` distinct package types to send out parcels. Some of these package types we use regularly, and others we use less often. We integrate our knowledge of how often a package type is used into the model by assuming the probability that the :math:`j`-th parcel will be of type :math:`k` is equal to :math:`\pi_k`:

  .. math:: \mathbb P(k_j = k) = \pi_k\qquad\forall j = 1,\dots,M,\;\forall k=1,\dots,K

We also integrate our beliefs about the volumes and weights of these different parcel types. We refer to the believed weight of the :math:`k`-th package type as :math:`\mu_{Z,k}` and the believed volume as :math:`\mu_{V,k}`. Further, we make use of our belief on how far the measured volume and weight of a parcel can deviate from the believed volume and weight by adding variance terms to this system with :math:`\sigma^2_{Z,k}` and :math:`\sigma^2_{V,k}`.  

If we know that a parcel item weighs :math:`X_{1j},\dots,X_{L_jj}`, and the parcel type weighs :math:`k_j`, then the parcel weight is a Gaussian random variable centered around the sum of the item weights and the assumed package weight :math:`\mu_{Z,k_j}`, with a variance determined by :math:`\sigma^2_{Z,k_j}`.

  .. math:: Z_j \mid X_{1j},\dots,X_{L_jj},k_j\sim\mathcal N\bigg(\sum_{l=1}^{L_j}X_{lj} + \mu_{Z,k_j},\sigma^2_{Z,k_j}\bigg)

The same idea applies to the parcel volume. We do not need to subtract the volumes of the individual parcel items, however, and so we get the formula:

  .. math:: V_j\mid k_j\sim\mathcal N(\mu_{V,k_j},\sigma^2_{V,k_j})
 
Article Weight
--------------

.. raw:: html 
  
  <object data="../images/weight-estimation/model4.svg" type="image/svg+xml" style="float:left; margin-right:10px; margin-top:5px">
    <img src="../images/weight-estimation/model4.jpg" />
  </object>
  
Let’s now switch focus from what we know about parcels to what we know about the hundreds of thousand of items in Zalando's inventory. We know there are :math:`N` different items. Further, we assume that the true (and unknown) weight of the :math:`i`-th article is :math:`X_i`. Lastly, we model the article weight :math:`X_i` as a Gaussian random variable, with mean :math:`\mu_{X,i}` and relative precision :math:`\rho_{X,i}`.  In formulas, this means

  .. math:: X_i\mid \mu_{X,i},\rho_{X,i}\sim\mathcal N\bigg(\mu_{X,i},\frac{\mu_{X,i}^2}{\rho_{X,i}}\bigg)
 
We use the precision :math:`\rho` instead of the more traditional variance :math:`\sigma` because it allows the variance to scale with the mean :math:`\mu_{X,i}`. Once we know :math:`\mu_{X,i}` and :math:`\rho_{X,i}`, we have answered the question we set out to solve and now have a reasonably accurate estimate about that particular article's weight.

Article Weight Hyper-Priors
---------------------------

.. raw:: html 
  
  <object data="../images/weight-estimation/model5.svg" type="image/svg+xml" style="float:left; margin-right:10px; margin-top:5px">
    <img src="../images/weight-estimation/model1.jpg" />
  </object>
  
All this wouldn't be Bayesian statistics if we didn't have a prior belief about the article's mean
weight and precision. Therefore, we introduce priors on :math:`\mu_{X,i}` and :math:`\rho_{X,i}`.

The prior on :math:`\mu_{X,i}` ensures that :math:`\mu_{X,i}` remains within the region of reasonable weight values (Zalando doesn't have any 1000 kg articles on sale). The prior on :math:`\rho_{X,i}` ensures that the random variable’s support doesn't become negative and retains enough variance to catch any fluctuations.

To make the solution more tractable, we decided to use the `conjugate priors <http://en.wikipedia.org/wiki/Conjugate_prior>`_
of :math:`\mu_{X,i}` and :math:`\rho_{X,i}`, meaning that for :math:`\mu_{X,i}` we use the `gamma distribution <http://en.wikipedia.org/wiki/Gamma_distribution>`_
as our prior setting:

  .. math:: \mu_{X,i}\mid\alpha_{\mu,X}\beta_{\mu,X} \sim \text{Gamma}(\alpha_{\mu,X},\beta_{\mu,X})
 
In the same way, we use the closely related `inverse gamma distribution <http://en.wikipedia.org/wiki/Inverse-gamma_distribution>`_
as a prior over :math:`\rho_{X,i}`, setting

  .. math:: \rho_{X,i}\mid\alpha_{\rho,X}\beta_{\rho,X} \sim \text{Inv-Gamma}(\alpha_{\rho,X},\beta_{\rho,X})
 
Putting It All Together
-----------------------

Now that we have a model for the parcels, and a model for the individual articles, it is not very
hard to glue them together. Assuming that if the individual parcel item :math:`X_{lj}` is of
article type :math:`i`, :math:`X_{lj}` and :math:`X_{i}` will have the same distribution:

  .. math:: X_{lj}\mid\mu_{X,i},\rho_{X,i}\sim\mathcal N\bigg(\mu_{X,i},\frac{\mu_{X,i}^2}{\rho_{X,i}}\bigg)
  
giving us the model we have been working towards this whole time:

.. raw:: html
  
  <object data="../images/weight-estimation/model15.svg" type="image/svg+xml" style="display: block; margin-left:auto; margin-right:auto">
    <img src="../images/weight-estimation/model15.jpg" />
  </object>
  
This model is optimized by

 * Estimating the values of :math:`X_{lj}`, :math:`\mu_{X,i}`, :math:`\rho_{X,i}`, :math:`k_j` via `Gibbs sampling <http://en.wikipedia.org/wiki/Gibbs_sampling>`_ 

 * Updating the hyperparameters to best explain the hidden variables

and repeating until convergence.

The Payoff
==========

Deriving our new measuring model took some effort! But it was all worth it, because now we have:

 * Automatic weight estimations for each Zalando article, which saves workers time
 
 * A reliable way to know the accuracy of our estimations

After working through this article, you deserve to give yourself a break.  So go ahead, take a look at (and like) `our old post <../posts/how-zalando-used-bayesian-statistics-to-find-free-money.html>`_ with all the fluffy text and pretty pictures. You’ve earned it.


___________________________________________

.. [Bishop] Bishop, Christopher M. *Pattern Recognition and Machine Learning*; Springer, October 2007.