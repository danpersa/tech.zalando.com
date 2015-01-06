<!--
.. title: Green or Orange? - A/B tests at Zalando
.. slug: green-or-orange-ab-tests-at-zalando
.. date: 2013-04-30 15:48:00
.. tags: ab-test,frontend,testing
.. author: Philip Harborth
.. image: ab-testing_teaser.png
-->

Have you ever wondered why
the orange button you always click on to put something in your shopping bag
has suddenly turned green? Probably not - we haven’t tested the button colour
yet but it could be a possible scenario for an A/B test. If you recognise
changes on our website along these lines, you may be part of a test.

<!-- TEASER_END -->

## Why do we run A/B tests?
The goal of A/B tests is to measure the effects of changes
based on the onsite management team’s ideas and theories. An example of an A/B
test is to test whether the green button works better than the orange button
that we currently have. But what does 'works better' mean in this case?

We use the results of these tests to influence our decision making - we want
to have proof that changing the button’s colour is the right way to go. That's
why we define key performance indicators (KPIs) and expected changes of these
values.

If the results of the analysis show an increase in the KPIs, we will implement
the change. If not, then our button is fine the way it is. In a test, you can
have multiple KPIs that are relevant for interpreting the results and,
ultimately, the judgement of which variant was ‘best’.

The best way to explain
exactly what we do when we run a test is to provide you with some examples. A
common scenario is to change positions, layouts or colours of certain elements
on the website. We also sometimes change wording and phrasing to find out
which words or tone has the most positive effect on users.

## Testing the wording of buttons
Last year, a new law was enacted in Germany to
regulate the wording of the button to complete an order on online shops. Words
like 'Order' or 'Continue' are now prohibited; instead online shops must use a
wording like 'Buy' or 'Buy now'. The wording should point out that an order is
associated with costs. There are many different wordings that fulfil the law
so we set up an A/B test with some variants to find out which wording is the
best for our shop and our customers.

The more visitors the page has, the
shorter an A/B test must run to reach significance. Actually, this is an
advantage of a popular website like Zalando: we have a large amount of
visitors so we get significant results in a very short period of time.

## Side effects
As a product manager, you must be aware of all side effects of a
test, be it technical issues or usability. After implementation, the code that
deal with the test is tested by our QA team. By using a special URL parameter,
they can define which variant of the test they want to see and check. This is
an important aspect of handling a test - normally the variants are randomly
allocated to users. The configuration defines, for example, that 10% of our
users should get variant A, 10% B and 10% C. But for testing a variant, it is
necessary to have the ability to force a variant. The configuration of these
percentages is done by using a Zalando tool, which we also use to start and
stop tests.

If you want to run an A/B test, the following components are very
important. First you need the functionality to assign users of your site to
the variants. You have to make sure that the amount of users really matches
the distribution you set up. You could run an A/B test without any changes on
the website for our control group to find out. Next, you should be certain
that the tracking works fine. You need all of the relevant tracking data to
calculate the pre-defined KPIs. It is also good to have the possibilty to do
an internal live test (e.g., the code for your the test is already live, but
no users have been assigned to the test). Using the described URL paraments
you can force a variant on the live environment and check if everything works
as expected.

## Participation - if you are lucky
Once an A/B test is active
and a user visits the Zalando website, the 'variant lottery' starts. The dice
decide if the user will take part in the test and, if so, which variant he
will see. This information is stored in the user session (for as long as the
test is active) so that a returning user will get the same variant he or she
saw the last time.

Due to the range of traffic we get during a week, we
normally run tests for a week or more, so that we have all weekdays in our
report. To create these reports, we use special analysis tools that help us to
establish which variant has won. When a test is switched off and we know the
winner, we will implement that variant as the standard version.

One problem of
A/B tests is the assignment of a variant to a user. Users might visit our
website from their own computer and then on another device, where they may be
shown another variant – in our example case, they will see the green button
and the orange button.

[![ab_testing_1](/files/2013/04/ab_testing_1.png)](/files/2013/04/ab_testing_1.png)

## New features
So, if you’re confused by
seeing different colours - relax, it’s probably an A/B test. With your
participation, we can gather more information about how users interact with
our website and optimise our site to account for this.

If you are a frequent
Zalando visitor and are chosen to take part in the 'variant lottery', you
could be one of the first users to explore a new feature on our site.

Keep your eyes peeled...

