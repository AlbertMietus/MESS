:orphan:
.. Copyright (C) ALbert Mietus; 2020
.. _startingWithBDD+TDD:

***********************
Starting with BDD & TDD
***********************

.. post:: 2020/07/01
   :tags: BDD, TDD
   :category: opinion
   :location: Eindhoven
   :language: en

   :reading-time: XXX

   Frequently I get questions on BDD or TDD especially on how to start.  And although there are no standard solutions,
   there are fascinating common grounds that I can share.

   Ideally, each team should understand the concept of this *development process* **first**, then **exercise** it,
   before practicing it in a **project**. In my humble opinion, that is hardly possible.  One can learn it “by doing”
   when being trained and coached.

Instructions too often focus is on using the tools. And automatically the goal becomes to blend those new tools into
the existing Way-of-Work (WoW). Eventually however, somebody will get disappointed; as the is no quality improvement, no
speed-up, nor any other improvement.
|BR|

But when no true goals are set, one shouldn’t complain when the expectations are not met!

So, what are the goals one can aim for?

.. sidebar:: WoW

   BDD and TDD should be *interwoven* with the typical steps in a development process, and will **change the order**!

   .. uml:: BDD+TDD-process.puml

===========================
What is What (Introduction)
===========================


A lot of opinions on BDD & TDD available; which can be confusing. Like with many modern-improvements, the words become a
hype to justify change without a proper need. That is not my goal. So let’s start with a summary, backed by the
definitions on Wikipedia.

TDD (`Test-driven development <https://en.wikipedia.org/wiki/Test-driven_development>`_)
========================================================================================

TDD is a *process*; where the tests are created **first** and the code second. One keeps executing all tests until the
code works. This is also a nice exit strategy.  Often, it is followed by one (short) refactor cycle: to tidy up the code
(and still passing the tests).

In practice, TDD is often/mostly used *Unit level* (one file, class, or function), by a programmer. But the concept
isn't restricted to that.

The are many variants, like **STDD** (system-level TDD), **ATDD** (Acceptance TDD), and **BDD**; the later is well known
popular.


BDD (`Behavior-driven development <https://en.wikipedia.org/wiki/Behavior-driven_development>`_)
================================================================================================

BDD is a variant of TDD focusing on the system (or business) level. Still, tests are written **first** and executed
*constantly*; when all tests are OK, the product-development is *"done"*.

Here, the testing focuses on the (top-level) requirements, the system, and/or business-features. Typically, they are
designed by test-professionals, system-architects or business-experts, and less technical. To be practical those tests
are written in a tool. They have to be executed frequently too.

Intermediates levels
====================

One can (should) practice this process for each “level in the V”.  Each classical *“test & integration” step* can be
split into a test-preparation and a test-execution activity.  The *preparation phase* becomes the **test-design**
activity, executed early and resulting in an ATS (Automated Test Script).  That ATS is executed frequently (at least
nightly) as soon as it is available. Continuously all ATSes are run on all levels, for all units, modules, services, and
systems; whether they are new, changed, or exiting. As is this automated, each run is for free.

This is valid for all levels: repeat running those ATSes.
|BR|
The practice implementation to create ATS for the various levels may depart. This will depends on the size of the
product, so on “the depth of the V”; on the background & environment of the teams; on there (technical) capability; etc.
One may see other tools, other skills, and often other people that become responsible.

Some like to introduce new, or more terms for each level or implementation-detail. I prefer to use the term ‘TDD’
generically, as the process is equivalent.
|BR|
Remember: changing it in name only, does not improve the process. As long as you reach your goals, I can live with
any name.


=====
Goals
=====
There are a few, generic, main goals:

1. Product-quality improvement: in short: better code and better products

   - TDD focuses more on the *‘bilitys’* of code: readability, testability, maintainability, ...
   - BDD is more product-level: “Does it do what is specified?”, and “Are  the specification correct?”

2. Process optimisation: reduce the cost of the development cycle.

   - The faster a bug is signaled, the cheaper is to repair.
   - Also see “exit strategy”, which is often forgotten.

=============
How to start?
=============

As BDD is a variant of TDD, and has a bigger (organisational) scope, it is often easier to start with TDD. This can be
done (on code/unit and/or module level) by an individual software-developer, or a (scrum) team.

Training & Mentoring
====================

Uncle Bob has several video's on TDD & BDD. See :ref:`UncleBobList_TTD+BDD` for an overview.


=============

As one can see,
   the order of the steps are changed: Testing (at all levels) is split into:

    - “TestDesign” (*prepare* & **automate**), and
    - “TestExecution” (no manual work; part of build-process)

    And one stats with the TestDesign (before and concurrent with the typical left side of the V). This make integration
    with SCRUM easy.

By storing the ATSes in version-controll maintenance of the tests is easy. When specifications change, some ATSes will
change. And

