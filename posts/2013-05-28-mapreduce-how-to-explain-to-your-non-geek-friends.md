<!--
.. title: MapReduce: How to explain it to your non-geek friends
.. slug: mapreduce-how-to-explain-to-your-non-geek-friends
.. date: 2013-05-28 10:08:54
.. tags: cluster,development,hadoop,mapreduce,node,parallelism
.. author: Luis Mineiro
.. image: hadoop_teaser.jpg
-->

Even though it's not something
new, the MapReduce concept was purely theoretical to me before I got to
Zalando. I did read [the paper](http://research.google.com/archive/mapreduce.html) more than once and I
had a pretty good idea when to use this kind of approach. My buddy Carsten
found [a very cool recipe](http://tech.zalando.com/fast-log-file-analytics-
with-python-and-sqlite/) for that quick 5min data analysis, but when you have
really huge datasets and not that much time, MapReduce is there to the rescue.

<!-- TEASER_END -->

The main use case for MapReduce is when the huge amount of data can be
processed in parallel. You’re probably asking... what kind of data is well
suited to be processed in parallel?

This is exactly what I want to share with
you. I've been working with [Hadoop](http://hadoop.apache.org/) frequently so
I decided to share my experience. Hopefully I'll help you get a clearer
overview of what it's all about, just like I would explain to my non-geek
friends.

So, what kind of data could we have at Zalando that should be
processed in parallel with Hadoop? We are generating a huge amount of log
files every day that hold valuable business metrics. For the sake of
simplicity I'll create a very simple scenario, which I believe, makes it
easier to understand how it works. Keep in mind the example is based on fake
data and the purpose is not the better way to achieve the goal but just to
demonstrate a comprehensive scenario.

## Short example

By the time I wrote this, Zalando was operationally active in Germany,
Austria, Switzerland, Denmark, Sweden, Norway, Finland, Spain, France, Italy,
Belgium, the Netherlands, Poland, and the UK. Let's assume we wanted those
countries grouped in 4 regions:
[![MapReduce: European regions](/files/2013/05/zalando_regions.png)](/files/2013/05/zalando_regions.png)

    Central Europe | Northern Europe | Southern Europe | Western Europe
    -------------------------------------------------------------------
    Germany        | Denmark         | Spain           | Belgium
    Austria        | Sweden          | France          | Netherlands
    Switzerland    | Norway          | Italy           | United Kingdom
    Poland         | Finland         |                 |

[![MapReduce: Sample data](/files/2013/05/region_values.png)](/files/2013/05/region_values.png)
Let's also assume our data is
based on this list of countries and that, for each country, we have two
attributes - the region it belongs to and the amount of purchases for a given
day.

This is some sample data where you can see the region and daily purchases
for each country. What we want to find out is the total amount of purchases
for each region. This is the interesting point where we should realize that
since we can group the countries by region, without caring about countries
from other regions, it is the perfect scenario to work the data in parallel.
The first step to get the total amount of purchases for each region is to
group the amount of purchases by region and then calculate the sum for each
group.

### Step 1 - Organize the data according to the region
[![MapReduce: Step 1 (Mapping)](/files/2013/05/map.png)](/files/2013/05/map.png)
We only care about the sum for each 
region so the data about the country name can be discarded. We'll only have
the region and the amount of purchases for each country.

### Step 2 - Group the values for each region
[![MapReduce: Step 2 (Shuffling)](/files/2013/05/shuffle.png)](/files/2013/05/shuffle.png)
Then we're able to join all those
values for the same region. The result will be a list of purchase amounts for
each region.

### Step 3 - Do the math for each region
[![MapReduce: Step 3 (Reducing)](/files/2013/05/reduce.png)](/files/2013/05/reduce.png)
You can see where this leads now. The
last thing to do is to calculate the sum for each of those lists. That's it!
This was MapReduce. A short step-by-step review:

  1. Organize the data according to the region
  2. Group the values for each region
  3. Do the math for each region

Really, it's that simple. And all of this would have worked in parallel, with huge amounts of data.

## MapReduce

Now let's try to establish a relation between all of this to their respective
MapReduce operations. As you have probably noticed, there are 3 stages during
a MapReduce operation: Map, Shuffle and Reduce.

### Stage 1 - Map
We had an input map with the country as a key and the tuple with region and
the amount of purchases as the value – `Map<Country, {Region, Purchases}>`. 
If you remember correctly we threw away the country name, as
we wanted to group the amount of purchases by region. From that step we got an
output map with a new key (the region) holding the amount of purchases (the
value) – `Map<Region, Purchases>`. This is what the Map part does. It
creates a new map with only the data that can be grouped, and is actually
relevant for us.

### Stage 2 - Shuffle
The shuffling takes this output and groups all the Purchases for the same
Region. We got a new map with the Region as the key and a list of Purchases as
the value – `Map<Region, List<Purchases>>`. MapReduce does this step
automatically so you don't have to worry about it.

### Stage 3 - Reduce
This new map from the Shuffle stage is the input for the last step – the
Reduce stage. As you probably figured out by now, all we had to do was to sum
all the Purchases on those lists. The output was another map with the Region
as the key and the sum of Purchases as the value – `Map<Region, SumOfPurchases>`.

### Putting it all together
Let's repeat the short step-by-step:

  * **Map** (organize the data according to the region) transforms the initial 
`Map<Country, {Region, Purchases}>` into a `Map<Region, Purchases>`
  * **Shuffle** (group the values for each region) groups all the Purchases for 
the same Region returning a `Map<Region, List<Purchases>>`
  * **Reduce** (do the math for each region) aggregates the data on each of those 
lists returning a `Map<Region,SumOfPurchases>` 

That's all there is to it. MapReduce makes all this pretty
easy. Using Hadoop you usually only have to override the Mapper's map() method
and the Reducer's reduce() method and adjust to your specific needs. You
could, for example, just change the reduce() method to calculate an average
instead of a sum. Everything else would stay the same.

The wonderful part about it is that everything is distributed across all the nodes in your
cluster, making it possible to perform this kind of calculation really fast,
and easy, with a real huge dataset.

If you're still not buying it, check out
these [amazing challenges](http://googleblog.blogspot.de/2008/11/sorting-1pb-with-mapreduce.html). 

_Map images courtesy of Google Maps and some Gimp wizardry_

