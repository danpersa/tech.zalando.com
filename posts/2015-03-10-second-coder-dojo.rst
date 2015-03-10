.. title: Test-Driven Development: A Zalando Coder Dojo
.. slug: test-driven-development-a-zalando-coder-dojo
.. date: 2015/03/10 08:00:00
.. tags: tdd, dojo, software craftsmanship, testing, pair programming
.. link:
.. description: Recap of the second Zalando Coder Dojo
.. author: Holger Schmeisky
.. type: text
.. image: dojo_tdd_cycle.jpg


=============================================
Test-Driven Development: A Zalando Coder Dojo
=============================================

Last week the Zalando tech team hosted our second Coder Dojo on pair programming and Test-Driven Development. (In software craftsmanship language, a coder dojo is a place where developers can train and practice their skills.) Similarly, we Zalandos use our Coder Dojos to practice programming without dealing with the pressures and restrictions of project deadlines and existing code bases.

.. TEASER_END

TDD is one of the most well-known practices of Agile Development. As a tech company that embraces Agile principles and best practices, we want to help our engineers to master the key Agile principles. The basic TDD workflow is as follows:
 
  1. Write exactly one new test
  2. Run the test to make sure it fails
  3. Write the least amount of code to make the test pass
  4. Refactor to improve the code
  5. Repeat the process

.. image:: /images/dojo_tdd_cycle.jpg
   :alt: The basic Test Driven Development cycle

First we started with a group warm-up exercise to help everyone who was doing TDD for the first time to get familiar with it. In this session, the group of us (about 20 engineers) tried to solve FizzBuzz--a very easy challenge, but one that allowed us to focus on the Test-Driven cycle. After 30 minutes and a lot of discussion about tests, test names and refactoring, we ended up at this solution (pull requests welcome!):

https://github.com/holger-s/fizzbuzz

Our 1st exercise focused on the Roman numerals kata, in which we converted integer numbers to Roman numerals:

http://agilekatas.co.uk/katas/romannumerals-kata.html

.. image:: /images/dojo_pair_discussing.jpg
   :alt: A pair discusses the algorithm for parsing numerals

For this exercise we paired up, sat down at our laptops, and tried to solve the exercise test by test. After 45 minutes of intense coding, we made it clear that nobody would have to deliver anything, and asked every developer to delete their code.

During the retrospective, our participants expressed mixed feelings about the exercise: 
  * No pair was able to convert complex Roman numerals like MMCMDCIX (3509). Most had succeeded in making tests for I, II V, X and XVI pass—typically by writing code to convert them to 1, 2, 5, 10, 14, respectively. 
  * The biggest challenge was to find the ideal moment for switching from very simple if-else implementations to using the actual algorithm and improving that incrementally. 
  * Most developers felt that writing down test cases first, then thinking about the design, would have been more effective.

In our next round, we asked the group to swap partners and either do an inverse version of the Roman numerals exercise with TDD (Roman numeral to integer), or try the first exercise from before again—this time without using TDD, using tests first, or undertaking a long design phase.

.. image:: /images/dojo_developers_working.jpg
   :alt: All developers are highly concentrated on the Kata


After 45 more minutes of intense coding, we asked everyone to delete their code again (and this time, everyone actually did!). Results from the retrospective:
  * One team described how TDD actually helped them to arrive incrementally at a beautifully simple solution for the Romans-to-integers problem
  * Teams that tried integers-to-Romans without TDD did not do as well as teams that used TDD 
  * Everyone still found it very hard to know how much to refactor and when

To wrap up the dojo, we had a general discussion of the TDD approach and concluded that, while TDD is useful in some cases, it is not always applicable and not easy. For example, one of the participants pointed out that he usually develops his Spring controllers in a TDD fashion:
  * Write a failing MockMVC test
  * Implement as much Controller code as necessary to make the test pass
  * Refactor

.. image:: /images/dojo_group_shot.jpg
  :alt: Group shot of dojo participants

After a few hours of hard coding, we relaxed with pizza and beer. To put it in the words of my favorite feedback Post-it: "It was fun!"

.. image:: /images/dojo_end.jpg
   :alt: How it ended
