<!--
.. title: Old school database access using stored procedures
.. slug: zalando-stored-procedure-wrapper-part-i
.. date: 2013-09-11 10:00:54
.. tags: backend,database,development,postgresql,sproc-wrapper
.. author: Jan Mußler
.. image: sproc-wrapper_teaser.jpg
-->

A few weeks ago we introduced
[PGObserver](http://github.com/zalando/PGObserver), hinting at the broad use
of stored procedures for accessing our data. Today, we will get into a bit
more detail about how and why we have chosen a different route back then and
continue to use stored procedures. To our new readers, for the Zalando
E-commerce Operating System ([ZEOS](http://tech.zalando.com/platform/))
platform we chose [PostgreSQL](http://www.postgresql.org) to store our
important data, spanning from customer order to article meta data. We did so,
because back then we trusted, and still do so, into this great open source
database, for its performance, reliability, and flexibility provided by a
large feature set including stored procedures in multiple languages.

<!-- TEASER_END -->

The decision to use [stored procedures](http://en.wikipedia.org/wiki/Stored_procedure) (SProcs) was
motivated by different aspects, including performance benefits and explicit
control over queries. Using stored procedures reduces the number of queries
issued by our Java application and lessens the amount of data transferred
between our database and application. Routing all access to underlying data
through our API also provides us with the necessary abstraction to change the
data structure and layout between releases. Additionally the API layer
combined with limited privileges provides additional safety and control over
changes in the database. Stored procedures also enable us to make some last
minute changes to the live environment due to their easy and fast deployment.
One last advantage I want to mention, is that stored procedures give you all
queries before you deploy, which is great for reviewing and performance
analysis. There are situations, where stored procedures require a lot of
additional work and yield less benefits, e.g., CRUD heavy applications with
lots of fields, where we have opened up the JPA / EclipseLink combo, with some
extensions for PostgreSQL specifics, as enums and array fields.

Looking back, using stored procedures was writing a lot of boiler plate code, creating
single classes for every procedure, writing type mappers from database result
to Java objects, writing annotations for input parameters and so on. But all
this changed, first two of our colleagues created the so called "typemapper"
that took care of reading PostgreSQL type information, reading Java
annotations and combining this to map stored procedure results to Java
objects. This was a big improvement, a lot of code was removed, there was not
any mapper code to write any more, and therefore the development became less
error prone to manual mapping errors.

Setting the goal higher, we wanted to write even less code and make using stored procedures in our sharded
environment comfortable, thus we implemented the "SProc Wrapper" for executing
stored procedures. Basically, you define a Java method in an interface, use
the proper annotations and from there the SProc wrapper takes over, deducing
type information and so on to correctly execute the right database procedure,
fetch the results, and map them back to the return type of the functions. This
brings down the amount of code to write for a single stored procedure to just
a few lines (one in the interface, and three more to be honest in the
implementation). Further the SProc wrapper gives you features to run a
procedure on a set of shards, select the shard automatically from "shard key"
fields, and "aggregate" in a sense of concatenating distinct results into one
result set. All of this proved really useful, due to our extensive use of
sharding.

And now one very basic example, first the PostgreSQL function,
supposing you are using 9.2 or higher: 

```sql
CREATE FUNCTION
compute_product(a int, b int) RETURNS bigint AS $$ BEGIN RETURN a * b; END; $$
LANGUAGE "plpgsql";
```

And finally the Java code:
```java
@SProcService
interface BasicExample {
    @SProcCall
    long computeProduct(@SProcParam int a, @SProcParam int b);
}
```

There is a bit more work involved setting up a data source and so on, but this example gives
you a good impression of how little code is necessary in Java for any
particular function.

And now the interesting part: you can find this on
[github.com/zalando/java-sproc-wrapper](https://github.com/zalando/java-sproc-wrapper), try it and tell us what you think! Or wait until we go into more
details in our follow up... :)

