.. title: Making Emotions Measurable
.. slug: zalando-making-emotions-measurable
.. date: 2014/10/21 10:00:00
.. tags: frontend,ab-test,testing,psychology
.. link:
.. description:
.. author: Carina Kuhr
.. type: text
.. image: making-emotions-measurable-1.png

Every day the userlab is supporting product teams in transforming their innovative ideas into new features for Zalando. To be able to answer all kinds of research questions about user behavior, we are continuously searching for interesting new testing methods and developments within our own field. Only then we can improve constantly.

.. TEASER_END

To answer a burning question about how good Zalando is in emotionally engaging the customer, we didn’t need to look far. A berlin based startup combines cutting edge testing techniques to show people's emotional reactions to visual stimuli in real-time.
We gave it a try by putting our new homepage designs and model pictures to the test.

Relevance of emotions
---------------------

From psychological research in advertising and marketing we know that emotions are a driving force when it comes to purchase decisions. Also, emotions are a crucial ingredient of the overall experience that is created when using a product (user experience). In the `user experience research <http://tech.zalando.com/posts/agile-ux-testing-at-zalando.html>`_  that we do in the UserLab, we examine emotions in the context of the human-computer-interaction (here the user-Zalando-interaction) where bad usability leads to frustration and a well designed interface meets the users expectations and adds to a satisfied customer. When we hear something like “Ok, honestly at this point I would just leave the page” we know that the design of the page is far from being ideal and that it obviously doesn’t create the positive shopping emotion that we were hoping for. We also know that an already frustrated and angry customer has a narrowed attention span and a particular strong need for easy findable information.

Recognizing emotions in users
-----------------------------

What we most often get out of user research is a good understanding of the user’s needs and motivations and the total UX package that a feature (-prototype) comes with.
When we let the users think aloud or observe their behavior in various situations, we can make educated guesses about their emotions by what they say, their tone of voice or their facial expressions. Also, there are numerous self-assessment tools (e.g. questionnaires) that let people indicate their emotional state. However, as psychologists we know that there is a lot more going on in the user’s mind that we don’t have access to and that is even unconscious for the user herself. Colors, designs or shapes affect the user on a whole different level and it is difficult to assess these affections with subjective and explicit methods like we usually apply in the UserLab. We can’t really tell what users feel when they first visit Zalando and are exposed to our teasers and model pictures before they even make the first conscious decision.
Because we wanted to take a deeper look into people’s immediate emotional responses to Zalando material, we tried a newly developed method. To understand how it works we have to make a brief excursion to the field of psychophysiology.

Assessing emotions with psychophysiological methods
---------------------------------------------------

This field of research knows and applies a couple of methods to study emotion and attention by measuring physiological responses (such as heart rate, brain activity or muscle activity) to stimuli. Basically this means that researchers draw conclusions on cognitive processes by studying for example the patterns in which neurons send out electrical and chemical signals
or by interpreting the rhythms in which the heart beats and the blood vessels constrict.

.. image:: /images/making-emotions-measurable-1.png

.. raw:: html

    <small>Source: http://emolyzr.de/</small><br>


The startup that I introduced in the beginning, uses two measurement methods of physiological activities to draw conclusions on emotional responses. One of them is called electromyography and assesses non-visible and unconscious movement of the facial muscles via electrodes that are placed in the participant's face (see photo). The rules are: if the risible muscle is active, something is perceived as attractive and if the corrugator muscle is active, something is perceived as unattractive. In addition to that, electrodes on the participant’s hand capture the conductance of the skin which is determined by the amount of induced sweat. This method is considered a sensitive measurement of the novelty of a stimulus.
The algorithm that the researchers of emolyzr developed uses data of both methods to compute a KPI that indicates the perceived attractiveness of websites or marketing material.  Eye-Tracking equipment records where people look at during an experimental session and the result is a heatmap like this one:

.. image::  /images/making-emotions-measurable-2.png

The emotions of Zalando customers
---------------------------------

This heatmap is an excerpt of emolyzr’s study report for Zalando and shows the aggregated data of 11 female participants that were invited to the lab at Humboldt University in August 2014 for a test case (please note that in a real study they involve 20-30 participants). The test subjects were exposed to different visual stimuli as websites, ads and commercials. According to the report, the pink areas show the elements of the page that triggered positive emotional reactions and the blue areas show the elements that triggered negative emotions. In addition the algorithm calculates scores for attractiveness, activation and overall emotional response that can be used to compare different versions. This design for example reaches a better overall score than the two other versions that were tested in this experiment and should therefore lead to higher conversion rates. Other versions showed a higher activation score. However, if it comes to the performance of online shops, activation should not be interpreted without the perceived attractiveness because high activation scores together with low attractiveness scores could rather lead to increased abandonment rates.

Despite the possible confounding factors the laboratory setting brings along, we are impressed by the method and the rich and detailed analysis of people’s immediate emotional reactions to our material that this way of measurement provides. We will take the results into account when we interpret our own `A/B test <http://tech.zalando.com/posts/green-or-orange-ab-tests-at-zalando.html>`_  materials of this test case as well as when we give recommendations on the design of future material.

