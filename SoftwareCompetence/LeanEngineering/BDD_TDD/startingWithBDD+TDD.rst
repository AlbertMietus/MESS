.. Copyright (C) ALbert Mietus; 2020
.. _startingWithBDD+TDD:

***********************
Starting with BDD & TDD
***********************

.. post:: 2020/07/15
   :tags: BDD, TDD
   :category: opinion
   :location: Eindhoven
   :language: en

   :reading-time: 5m30

   Frequently I get questions on BDD and TDD by example on how to start. And although there are no standard solutions,
   there are fascinating common grounds that I can share.

   Ideally, each team should understand the concept of this *development process* **first**, and  then **exercise** it,
   before practicing it in a **project**. However, it is also possible to learn it ‘by doing’ when being trained and
   coached; in my humble opinion.

Instructions too often focus on using the tools. And almost automatically, the goal becomes to blend those new tools into
the existing Way-of-Work (WoW). Eventually, however, somebody will get disappointed; as there is no quality improvement,
no speed-up, nor any other improvement.
|BR|
But when no true goals are set, one shouldn’t complain when the expectations are not met!

So, what are the goals one can aim for?

.. sidebar:: WoW

   BDD and TDD should be *interwoven* with the typical steps in a development process, and will **change the order**!

   .. uml:: BDD+TDD-process.puml

===========================
What is What (Introduction)
===========================

There are a lot of opinions on BDD and TDD, which can be confusing. Like with many modern-improvements, words often
become a hype to justify change without a proper need. That is not my goal. So let’s start with a summary, backed by the
definitions on Wikipedia.


TDD (`Test-driven development <https://en.wikipedia.org/wiki/Test-driven_development>`_)
========================================================================================

TDD is a *process*; where the tests are described **first** and the code second. One keeps executing all tests until the
code works. This encourages also good habits as *refactoring*: the risk to inserti a bug is minimal. TDD also provides
a nice *exit strategy* (see below).

In practice, TDD is often/mostly used *Unit level* (one file, class, or function), by a programmer. But the concept
isn't restricted to that.

The are many variants, like **STDD** (system-level TDD), **ATDD** (Acceptance TDD), and **BDD**; the later is well known
and popular.


BDD (`Behavior-driven development <https://en.wikipedia.org/wiki/Behavior-driven_development>`_)
================================================================================================

BDD is a variant of TDD focusing on the system (or business) level. Still, tests are written **first** and executed
*constantly*; when all tests are OK, the product-development is *done*.

Here, the testing focuses on the (top-level) requirements, the system, and/or business-features. Typically, they are
designed by test-professionals, system-architects or business-experts, and less technical. To be practical those tests
are written in a tool. They have to be executed frequently too.

Intermediates levels
====================

One can (should) practice this process for each ‘level in the V’.  Each classical *’test & integration’ step* can be
split into a test-preparation and a test-execution activity.  The *preparation phase* becomes the **test-design**
activity, executed early and resulting in an ATS (Automated Test Script).  That ATS is executed frequently (at least
nightly) as soon as it is available. Continuously all ATSes are run on all levels, for all units, modules, services, and
systems; whether they are new, changed, or exiting. As is this automated, each run is for free.

This is valid for all levels: repeat running those ATSes.
|BR|
The practice implementation to create ATS for the various levels may depart. This will depend on the size of the
product, so on ‘the depth of the V’; on the background & environment of the teams; on there (technical) capability; etc.
One may see other tools, other skills, and often other people that become responsible.

Some like to introduce new, or more terms for each level or implementation-detail. I prefer to use the term TDD
generically, as the process is equivalent.
|BR|
Remember: changing it in name only, does not improve the process. As long as you reach your goals, I can live with
any name.


=====
Goals
=====
There are a few, generic, main goals:

1. Product-quality improvement: in short: better code and better products

   - TDD focuses more on the *abilities* of code: readability, testability, maintainability, ...
   - BDD is more product-level: “Does it do what is specified?”, and “Are the specification correct?”

2. Process optimisation: reduce the cost of the development cycle.

   - The faster a bug is signaled, the cheaper is to repair.
   - TDD also provides an *‘exit strategy’*; an often forgotten “side-effect” increasing velocity.

Exit strategy (lean summary)
============================

One often overseen goal is the implicit *exit strategy*, that comes for free with (all variants of) TDD. A :ref:`blog
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

=============
How to start?
=============

Back to the main question: how to start?
|BR|
Whenever the goal is: *use new tools*, it is simple: purchase them, shop for some hands-on training, and you are done.

With a goal as described above: one has to discipline the team. And **unlearn** old habits as spend-up the ‘left
time’. That is a lot harder, as nobody is wasting time! (Remember: *improving ‘abilities’ is worthwhile*, and a TDD
goal!)

As BDD is a variant of TDD and has a bigger (organisational) scope, it is often easier to start with TDD. This can be
done on unit/file, and/or module level, by one individual software-developer, or by a single (scrum) team.

TDD on TDD
==========


Let’s start with a test, as TDD describes. But now on the process-improvement itself.  Now we have set the goals, its
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


--- :CGE-email:`Albert.Mietus`

