:orphan:

TODO (in Lean Engineering)
==========================

This is a landing page for links to future articles (or blog). There is no timeline :-) So maybe once ...

.. _tdd_exitstrategy:

The *Exit Strategy* of TTD [ToDo]
---------------------------------

The agile concept of *Test Driven Development* is also **Lean** practice, as it clearly defines when a developer is
ready: when all test pass.  Many developers assume the can use all time as set in the planningsession; but that is
wrong!

The Time to Complete (T2C) of a task is an average. So, halve takes (a bit) longer, and halve can be done quicker --see the bell curve.

.. todo:: Exit strategy (lean summary)

   One often overseen goal is the implicit *exit strategy*, which comes for free with (all variants of) TDD. A
   :ref:`blog <TDD_exitStrategy>` on that will be posted later, but let’s give a summary already.

   Engineers tend to overreach their obligations, especially when there is some planned time left. Then, there are
   always ways to improve and extend the code. Good programmers always have the ambition to improve on readability,
   maintainability, etc. This sounds positive (and it is), but has an indirect negative effect on cost.
   |BR|
   As (scrum-poker) estimations are based on averages, probably half of the tasks are a bit less work as assumed, and
   the other fifty percent takes a bit more. However, when the ‘left time’ is used for improvements, there is no spare
   to make up the overrun tasks. And oddly enough, they are always at the end.

   So, the question become: *“How can we be lean on the first 50%, to use the ‘spare time’ for the remaining 50%?”*
   |BR|
   With TDD, a task is done when the tests pass!

   That means a developer got a clear indication (s)he is done. As soon the lights are green, it is time to move on!
   Probably a few ticks of labor are left: like tidy-up, review, and a pull-request the new feature.
   |BR|
   By having an objective signal to expire an assignment, even when there is ‘time left’, and assuming the (average)
   estimations are correct, all tasks will be on time (on average). And although this sounds as normal, the experience
   of many teams differ.


--
