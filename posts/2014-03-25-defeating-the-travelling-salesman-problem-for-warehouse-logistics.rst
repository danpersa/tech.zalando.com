.. title: Defeating the Travelling Salesman Problem for Warehouse Logistics
.. slug: defeating-the-travelling-salesman-problem-for-warehouse-logistics
.. date: 2014-03-25 10:15:12
.. tags:
.. author: Calvin Seward
.. image: warehouse.png

Let’s say you know what items need to be retrieved from a warehouse and you know where the items are located. But can you retrieve all those items following an
optimal route? Now further assume that you are using a cart to collect the items, can you also figure out how to optimally manage the cart, too? “Of course not!,”
you cry, “Calculating the optimal route is the `travelling salesman problem <https://en.wikipedia.org/wiki/Travelling_salesman_problem>`_, and as to solving
the problem with the cart, now that would be pure black magic.” Don’t believe me? Try your luck with the picture below, see if you can find the shortest route that
passes by all the x-marks. At Zalando we have developed an efficient algorithm to solve just this problem, and today we’ll tell you more about it.

.. TEASER_END

The Travelling Salesman Problem in Logistics
--------------------------------------------

When an order is placed at the Zalando shop, the items don't just appear by magic at the doors of screaming customers like in the Zalando commercials, but the work is done in multiple steps in Zalando's warehouses. One of the steps is the so called “pick” step.  In this step, a worker retrieves a bunch of items from a large
hall filled with shelves of clothes, shoes and accessories. The hall is not unlike a large supermarket where shelves are arranged and separated by aisles and cross
aisles. The worker retrieves the items by picking up an empty cart and going from location to location as instructed by his bar code scanner, not unlike a shopper picking up all the items on his shopping list.  Once he has retrieved all the articles in his tour, he returns the full cart and starts on a new list. A figure of the situation can be seen below, where the x’s denote locations where the worker must
retrieve an item, and the node at the very bottom is where he picks up and drops off his cart.

.. image:: /images/pick-steps.png
   :alt: Pick position and route

Clearly the distance the worker has to walk for a tour depends heavily on the order in which he retrieves all his items. An experienced customer in our
supermarket example doesn't work through his shopping list in the order he has written the list, but he works through the list dependent on where the items are in
the supermarket in order to minimize his travel time.  The goal of ourproject was thus to order the worker's list of locations such that he takes the route with
the minimal travel time.  Solving this problem is equivalent to solving the travelling salesman problem in a special form.

It is generally known that the travelling salesman problem is NP-hard in its unrestricted form, meaning that it can not be solved efficiently for large scale
problems. And if it is not solved, the route that the workers walk is longer than it needs to be.  We calculated that such inefficiencies were causing our workers
to walk 40,000 extra kilometers each year, meaning they walked around the world simply because we couldn’t tell them the best route to walk.

It is also known that there are many special cases where the travelling salesman problem can be solved with polynomial complexity. Therefore, just because a
problem is a travelling salesman problem doesn't mean all hope is lost. Over the last few months, my team implemented a linear complexity solution to a special
case of the travelling salesman and extended it to also help the worker manage his cart.

Calculating the Optimal Route Without a Cart
--------------------------------------------

Luckily, our warehouse configuration is a special case that can be solved in polynomial time and where an algorithm to do this has already been published. Therefore we were able to implement an
already existing algorithm in order to minimize the worker's travel distance.  The details of the exact algorithm are discussed in this paper [#]_ (or the free version `here <http://www.roodbergen.com/publications/EJOR2001.php>`_). Please be warned that,
in order to understand the first paper, it is very helpful to read this paper [#]_  detailing the even simpler case of a warehouse without a cross aisle.

By implementing this algorithm, the optimal travel time problem is not yet fully solved since in our case minimizing travel distance doesn't always minimize travel time.  Consider yet again our
intrepid shopper in the supermarket.  If he is particularly hungry, then he will pick up a shopping cart before he collects all the items he wishes to purchase.  And since the shopping cart is
slow and unwieldy, he will often times leave it in the cross aisles, pick up a few items and return to his cart.  By not having to take the cart with him everywhere, he reduces his travel time
while increasing his travel distance.

Calculating the Optimal Route With a Cart
-----------------------------------------

Thus, the last step of our project was to develop an algorithm that gives the worker hints about where to move and leave the cart so that his overall travel time is optimized.  In order to create
an algorithm that does this, we built on the paper from above by adding more rules to ensure that the routes created with the cart were valid and more logic to calculate the travel speed of the
picker with and without the cart.

After doing all this, we had an algorithm that could calculate the optimal route that a warehouse worker had to take, and where he should leave and pick up his cart.  The optimal route for the
warehouse above can be seen below, with the dark lines representing the path that the cart takes, and the light lines the path that the worker takes.

.. image:: /images/pick-steps-2.PNG
   :alt: Shortest walk with cart positions

It is nice to know that, even though we didn't solve the general travelling salesman problem in polynomial time, we did manage to make it reveal its secrets for one special case and were able to apply that knowledge to an issue of great relevance: our order fulfillment efficiency, a must-have for success in online retail.

___________________________________________

.. [#] Kees Jan Roodbergen, René de Koster, Routing order pickers in a warehouse with a middle aisle, European Journal of Operational Research, Volume 133, Issue 1, 16 August 2001, Pages 32-43, ISSN 0377-2217
.. [#] \H. Donald Ratliff and Arnon S. Rosenthal, Order-Picking in a Rectangular Warehouse: A Solvable Case of the Traveling Salesman Problem, Operations Research, Vol. 31, No. 3 (May - Jun., 1983), pp. 507-521
