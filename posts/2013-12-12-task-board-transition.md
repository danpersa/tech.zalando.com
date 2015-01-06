<!--
.. title: Task Board Transition
.. slug: task-board-transition
.. date: 2013-12-12 10:01:46
.. tags: task-board,jira,kanban,agile
.. author: Lothar Schulz
.. image: 20131025_094912_teaser.jpg
-->

**Do you prefer an analog task board over a digital one?**

I did prefer an analog task board mainly for the
following reasons:

  * Moving a sticky note from one column to another is a physical process. Particularly putting it into done column feels simply good
  * Doing the stand up in front of a board supports the intention of our stand up meeting:
  * Talking about what was reached yesterday
  * What is going to happen today in order to meet the iteration deadline

Over time I realized there might be advantages of a digital board. As we use
Jira to track (development) tickets, every ticket is doubled in Jira and on
the analog board. This is because tickets are a base for reports and
references to other teams. Using a digital board simply saves time and effort
of maintaining the status of every ticket twice. Based on this, the proposal
to change to a digital board was kind of natural. Replacing the analog task
board with something else was easy because the project team I am part of works
on a project that will be finished sooner or later anyway. Even if we found
out, a digital board was not a good idea, the board as well as the project
will be done at one point in time.

<!-- TEASER_END -->

[![analog board](/files/2013/12/20130917_122710.jpg)](/files/2013/12/20130917_122710.jpg)

These are the steps of transition we did:

  1. Identify options Jira offers for such a board
  2. Do the first test board and play around
  3. Find out how to control iterations
  4. Put it on a (big) screen
  5. Start using it

Here some details about the transition steps.

## 1. Jira options

There are 2 board options Jira offers out of the box:

  * Kanban Board
  * Scrum Board

We went for the kanban board, because we have parrallel iterations running at
the same time in our team. The scrum board was not an option because you can’t
have parallel active scrums. I really like the planning mode of scrum boards
though. The way how to prioritize tickets using drag and drop is simply
convenient. Certainly you can do similar prioritization with Kanban boards
too.

## 2. First board

Creating the first kanban board was straight forward. As we used already a
couple of Jira filters for other purposes, I based the first test board on
existing filters. Filters are also a way to deal with the 3rd point of the
transition list:

## 3. Iteration controlling

Swimlanes are a good way to represent iterations in a kanban board. We used
epics already on the analog board as container of a couple of tickets within a
certain time frame / iteration. Swimlanes are actually Jira filters. So we had
to combine existing epics with appropriate filters. There are ( at least )
three ways to create a filter that represents all the tickets of an epic:

  1. _"Epic Link" = [your Jira epic ticket ID] e.g. "Epic Link" = ZEOS-22910_
  2. _key in ([list of Jira tickets belonging to an epic]) e.g. key in (ZEOS-21639, ZEOS-22022)_
  3. _issue in linkedIssues([your Jira epic ticket ID] ,"contains") e.g. issue in linkedIssues(ZEOS-25047,"contains")_

I identified those options in this order, because only the last one was easy
enough to use. The first way did not work for me. I had a hard time to find
out why and could essentially not find the underlying reason. So I switched to
the second way. When I was playing around with the second way, I was told the
first way could work after a Jira admin task has been performed. When this
admin task was about to be performed, I was lucky enough to get another tip:
the third way. This way works w/o long lists of tickets, just with the epic
ticket number. Out of the three identified ways, a string like "contains"
feels most natural to me. So this it is still the way I define swimlanes.
Tickets can be contained in a specific epic are rarely contained by another
epic (that means, the team often meets the target of the iteration). We
experienced those tickest always in the newer epics on the board. As this was
never an issue for us, I did not spend time if we should change something.

I mentioned earlier parallel iterations. In a nutshell, those are the three
iterations that run in parallel:

  * Specifying tickets
  * Developing tickets
  * QAing tickets

A ticket is specified in the week before it gets developed. The QA week of
such a ticket follows the dev week. Tickets to be specified are held in a
column labeled **analysis/spec**. The gateway between tickets being part of
the spec iteration to the dev iteration is the column **ready4dev**. Once a
ticket is picked from this column, it is part of the dev iteration,
represented by the column **in dev**. Column **QA todo** is the gateway as
well as it represents the QA iteration. Once a ticket is considered done for
the whole team, it is part of the column **QA done**.

## 4. Do the stand up in front of screen

Having the new board in Jira is good. However it is much more valuable if we
can do our daily stand up in front of the new board. We got a reasonable
screen that let us almost forget the former task board. [![stand up in front
of the digital board](/files/2013/12/20131025_094912.jpg)](/files/2013/12/20131025_094912.jpg)

## 5. Live

The digital board is in use for a couple of weeks now. The main pain point (tracking 
the status twice: on the analog board and in Jira) is still the main
reason to use the digital board. Jira is the only place to track the status of
a ticket for all of us, PMs, Devs and QAs.

In a nutshell, the digital board works better for the team.

Additionally I can double check the status of the
board when I am in meetings and might be asked about the status of tickets.
Changing the boards structure such as including new columns is also an easy
task with the new board.

## Anything else?

With the help of our Jira support team, we got a general Jira user with
appropriate rights to move tickets in our stand up meeting. The Jira project
workflow defines much more ticket statuses then there are columns in our
digital board.

This sample highlights the situation: The statuses "In
Progress" and "Developer Test" are mapped to the board column "In Dev". The
following board column is "QA Todo". This column is mapped to ticket status
"Ready 4 QA".

        |                | In Dev | QA Todo |
        | -------------- | ------ | ------- |
        | In Progress    | x      |         |
        | Developer Test | x      |         |
        | Ready 4 QA     |        | x       |

Moving a ticket on the board using drag and drop with status "Developer Test"
from column "In Dev" to "Ready 4 QA" is possible. This is because the status
transition (from "Developer Test" to “Ready 4 QA") directly applies to a
column transition (from "In Dev" to "QA Todo").

In contrast, you can’t move a ticket on the board with status "In Progress" from column "In Dev" to "Ready
4 QA", because a ticket has to transfered to status "Developer Test" before
you can change the status to "Ready 4 QA".

There is only one owner per kanban
board. This implies only this user can adapt the board e.g. adding new
swimlanes. As I am mainly responsible for the Jira tickets, I am also the
owner of the board. This subject became not an issue yet, because I was absent
only a couple of days since the digital board was used in the daily standup.
However one possible workaround for the only-one-board-owner issue could be to
use the general Jira user that also allows to move tickets. So far we did not
tried it yet.

There are other teams at Zalando that work with two boards, a
digital and an analog one showing the same tasks. Those teams do not feel the
need to switch only to a digital board. The doubled effort of maintaining
tickets twice is reduced as the sticky notes on the analog board are used as
summaries. Moreover the extra effort feels worth for them the satisfaction of
putting a ticket manually to 'done'. They also feel this helps both, product
managers and developers, to improve ticket progress maintenance.

## Take aways

The whole board transition last for our team only for a couple of days. From
this point on, there was no need for our project team to go back to the analog
board anymore.

However I believe both, an analog board as well as a digital
board, does make sense under different conditions and in other environments.
I'm happy I started the transition and learned a lot during the transition
process, independent from the result. Hence every team should decide which
board works best to support their tasks.

