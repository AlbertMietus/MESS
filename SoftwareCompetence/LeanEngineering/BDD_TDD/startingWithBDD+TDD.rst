.. Copyright (C) ALbert Mietus; 2020, 2023
.. _startingWithBDD+TDD:

*******************************
Starting with BDD & TDD (DRAFT)
*******************************

.. post:: 2020/07/15
   :tags: BDD, TDD
   :category: opinion
   :location: Eindhoven
   :language: en

   :reading-time: 5m30

   Frequently I get questions on BDD and TDD, like how to start. Although there are no standard solutions, there are
   fascinating common grounds that I can share.
   |BR|
   The key is simple: understand the goals.

   Typically engineers are clever: When they understand the objectives, they will find a solution; that is their job!

   .. update:: 2023/04/30

      As it is still actual and fits in my new :ref:`MESS_blogs`, I made a few updates and reposted it.

Ideally, each team should understand the concept of this *development process* **first** and then **exercise** it before
practicing it in a **project**.  However, IMHO, it is possible to learn it on the job. As long as one is carefully
trained & couched while practicing.
|BR|
A pitfall is to focus on the tools and learn new tricks. That hardly ever makes a process lean.

Instructions too often focus on using the tools. And almost automatically, the goal becomes to blend those new tools into
the existing Way-of-Work (WoW). Eventually, however, somebody will get disappointed. There will be no quality improvement,
no speed-up, or any effect.

.. tip:: Without set goals, one shouldn't complain when expectations are not met!

So, what are the goals one can aim for?
|BR|
Simple: a more Lean & Agile approach.

Or even bolder: Design (aka write) an (embedded software) product that fits the needs of the end-users better, with
no flaws, in less time and with less effort (cost).

.. sidebar:: WoW

   BDD and TDD should be *interwoven* with the typical steps in a development process and will **change the order**!

   .. uml:: BDD+TDD-process.puml


===========================
What is What (Introduction)
===========================

There are a lot of opinions on BDD and TDD, which can be confusing. As in many modern improvements, words often become
hyped to justify any change. That is not my goal. So let’s start with a summary backed by the definitions on Wikipedia.


TDD (`Test-driven development <https://en.wikipedia.org/wiki/Test-driven_development>`_)
========================================================================================

TDD is a *process*; where the tests are described **first** and the code second. One keeps executing all tests until the
code works. This encourages good habits such as *refactoring* also.
|BR|
Change code is constantly tested, so the risk of inserting a bug is minimal.

TDD is typically practiced at the unit level (one file, class, or function), where the programmer writes test and
production code in a short loop (a minute)
|BR|
The are many variants, like **STDD** (system-level TDD), **ATDD** (Acceptance TDD), and **BDD**; the latter is
well-known and popular.

TDD also provides a nice *exit strategy* (see below).

BDD (`Behavior-driven development <https://en.wikipedia.org/wiki/Behavior-driven_development>`_)
================================================================================================

BDD is a variant of TDD focusing on the system (or acceptance) level. Again, tests are written **first** and
executed *constantly*; when all tests are OK, the product development is *done*.

Here the testing focuses on the (top-level) requirements, the system, and/or business features. Typically, they are
designed by test professionals, system architects, or business experts. They are less technical compared with
TDD tests. And, to be practical, those tests are written in a dedicated tool; using a high-level *“almost English”
language*.

As the size of the change is bigger -- like a feature or user story-- the cycle is (also) longer. Typically a few days.

Like with TTD, BDD tests are executed frequently.
|BR|
Some prefer to “enable” new tests only when the feature is coded -- this prevents a failing test (as the production code
isn’t done). IMHO, one should avoid this. One should run the tests but in a lower urgency branch. And promote both to a
higher level when integrating (see an upcoming blog on this).


All levels
==========

One can (should) practice this process for all *levels in the V*.

Each classical *’test & integration’ step* can be split into a test preparation and an execution activity.  The
*preparation phase* becomes the **test-design** activity, executed early and resulting in an ATS (Automated Test
Script).
|BR|
That ATS is executed frequently (at least nightly) as soon as it is available.

Executing all tests at all levels for all units and modules and for every story and feature verifies everything. This
covers pure integration errors.  This covers pure integration errors but is also a safety net when mistakes are not
found at a lower level.

Remember: those ATSes run fully automatically. So, the cost of all those executions add-up to almost nothing.

====================================
Why not just write and run the test?
====================================

TTD and Unit Tests are related, but not the same!
|BR|
When practicing TDD, the focus is on preventing flaws, not finding them.TDD is a process that dictates when
to write a test (first), when to write production code (second), and when to execute the tests (constantly and
automatically).

The same applies to BDD, even though the frequency is a bit slower.

Developer versus Team
=====================

TDD and BDD act on different levels. TDD is typically at the bottom of the *’V’*; BDD is more at the system (or
acceptance) level.
|BR|
However, that is often confusing for new adopters.

Therefore I often use a more pragmatic distinguishment: Individual Developer versus (scrum)Team.
|BR|
A single developer can act following  TDD. (S)he writes code, tests and production code and switches between them
every minute. As TDD is more productive, hardly anyone will notice it when somebody “secretly” adopts TDD. No
extra tools or frameworks are essential.

That is hardly possible with BDD, as this is at the team level. A developer can’t run an acceptance test without the
assistance of a tester designer.
|BR|
Despite this, a single team can embrace BDD -- even when others don’t

This is valid for all levels: the larger the part that is worked on, the more commitment needs to be able to run those
ATSes.

Testability
===========

Everbody knows some code that is hard to test. I have seen functions without input or output -- the purely act on
global state (global variables). We know that is bad, but is also untestable.
|BR|
We should avoid that.

By writing test first, we enforce an implicit requirement: code should be testable.

=============
How to start?
=============

Back to the main question: how to start?
|BR|
Whenever the goal is: *use new tools*, it is simple: purchase them, shop for some hands-on training, and you are done.

In real life, you need to set goals first, and constantly measure whether your reached them.
|BR|
Sound familiar? That is essentially TDD!

  Every body has it own gaols 

Goals
=====
There are a few, generic, main goals:

1. Product-quality improvement: in short: better code and better products

   - TDD focuses more on the *abilities* of code: readability, testability, **maintainability**, etc.
   - BDD is more product-level: **“Does it do what is specified?”**, and “Are the specification correct?”

2. Process optimisation: reduce the cost of the development cycle.

   - The faster a bug is signaled, the cheaper is to repair.
   - TDD also provides an *‘exit strategy’*; an often forgotten “side-effect” increasing velocity.

Exit strategy (lean summary)
============================

One often overseen goal is the implicit *exit strategy*, which comes for free with (all variants of) TDD. A :ref:`blog
<TDD_exitStrategy>` on that will be posted later, but let’s give a summary already.

Engineers tend to overreach their obligations, especially when there is some planned time left. Then, there are always
ways to improve and extend the code. Good programmers always have the ambition to improve on readability,
maintainability, etc. This sounds positive (and it is), but has an indirect negative effect on cost.
|BR|
As (scrum-poker) estimations are based on averages, probably half of the tasks are a bit less work as assumed, and the
other fifty percent takes a bit more. However, when the ‘left time’ is used for improvements, there is no spare to make
up the overrun tasks. And oddly enough, they are always at the end.

So, the question become: *“How can we be lean on the first 50%, to use the ‘spare time’ for the remaining 50%?”*
|BR|
With TDD, a task is done when the tests pass!

That means a developer got a clear indication (s)he is done. As soon the lights are green, it is time to move on!
Probably a few ticks of labor are left: like tidy-up, review, and a pull-request the new feature.
|BR|
By having an objective signal to expire an assignment, even when there is ‘time left’, and assuming the (average)
estimations are correct, all tasks will be on time (on average). And although this sounds as normal, the experience of
many teams differ.

------------

With a goal as described above: one has to discipline the team. And **unlearn** old habits as spend-up the ‘left
time’. That is a lot harder, as nobody is wasting time! (Remember: *improving ‘abilities’ is worthwhile*, and a TDD
goal!)

As BDD is a variant of TDD and has a bigger (organisational) scope, it is often easier to start with TDD. This can be
done on unit/file, and/or module level, by one individual software-developer, or by a single (scrum) team.

TDD on TDD
==========


Let’s start with a test, as TDD describes. But now on the process improvement itself.  Now we have set the goals, its
easy to transform them into tests. Or, possibly a timeline of intermediates goals. Each goal needs some tests. Probably
not as exact as we like with typical *ATSes*, but ar least clear and “SMART”.

As you have your own goals, you need your distinct test-set. But assume you would like to improve both on quality and
productivity. Then a simple testable goal is the number of issues found “after” the sprint ends.  When this becomes zero
your quality-goal is met.
|BR|
And the velocity-increment is a great measure for productivity growth.

I would introduce some simple transitional goals too. Like, the number of flaws the QA-department finds should go down
*every* iteration. And *each* sprint the number of unfinished features should lower first, and the number of fully
correct features should fo up, secondly.

This sounds simple. And it is, except for the first time!
|BR|
Having a (quite) objective test does help, but the hard work is to improve yourself. To get comfortable with the new,
initially counter-intuitive routines will take practice and time.

But at least you have a great start!

Training & Mentoring
====================

Engineers are awesome in problem-solving. And although a quest like “start with TDD” is nebulous, when transformed into a
problem they like to fix it.  Especially when you give them some assistance and a sound target like passing a test.
|BR|
With the ‘TDD on TDD’ trick, you are ready to finish.

There are many books & and videos on TTD. They can help to start. As a downer, they focus often on classical ICT, not
high-tech, embedded product development. And so, they often don’t inspire.
|BR|
Also, many books are on ‘*How’* to do TDD, on using a tool.

Engineers like to understand ‘**WHY**’. Then, the can deal with the issue.

Uncle Bob
---------
Uncle Bob has several videos on TDD and BDD. See :ref:`UncleBobList_TTD+BDD` for an overview. Start with the basic TDD (6.*)
ones! They explain the ‘Why’.

.. hint::

   Most examples are in Java, and not very technical. This is fine for a start. Still, I would love an ‘add-on’ on the
   typical high-tech, embedded, product-development aspects; but that is not available.


Intervision & coaching
----------------------

A very effective, lean, and iterative concept I practice is *Video-of the week*.
|BR|

A group of people watches that selected video and at the end of the week, we speak about it for an hour and a half;
shared in the pre-corona era. Now it’s on-line, both work fine.

By having a group of mixed experiences, backgrounds, and ages, that *debriefing* becomes very encouraging and brings a huge
value.

.. tip::

   When you like to start with TDD or BDD or when you think about it, but don’t know ‘why’, or ‘how to start’: Give me a
   call. I will gladly boost your product and team.


--- :SwBMnl-email:`Albert.Mietus`



..  LocalWords:  distinguishment

----

The practice implementation to create ATS for the various levels may depart. This will depend on the size of the
product, so on ‘the depth of the V’; on the background & environment of the teams; on their (technical) capability; etc.
One may see other tools, other skills, and often other people that become responsible.

Some like to introduce new, or more terms for each level or implementation detail. I prefer to use the term TDD
generically, as the process is equivalent.
|BR|
Remember: changing it in name only, does not improve the process. As long as you reach your goals, I can live with
any name.
