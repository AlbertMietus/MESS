.. Copyright (C) ALbert Mietus & Sogeti.HT; 2020

.. _all_graph:

All needs [BigTree]
===================

We can also show the relations between all product (cq releases) and it *needs* in one big tree [#forrest]_.

.. needflow::

Lessons learned
---------------

#. We have at least one test-case for each requirement; as we can clearly see.
#. The “puzzling” specification for :need:`CALC2` have an affinity with both the requirements and the test-cases
#. The (general) requirements for both calculators are equal.
#. Both calculators are akin; :need:`CALC2` is kind of a enhanced version of :need:`CALC1`

This “BigTree” gives a global overview of all ‘needs’ and there relations; which gives insight into product and how to
test it. It can be generated when the requirements (and other ‘needs’) are affixed with their (outgoing) links.
|BR|
Even when the number of ‘needs’ becomes huge, this graph can be drawn quite clear -- although you make like to use a big
slide of paper.

It will directly shown some “isolated” requirements or test, when you forgot to add a link. Also other “curious looking”
parts of the drawing may need some attention. As it remarkable often denotes some mistakes.

.. rubric:: Footnotes & Links

.. [#forrest] In general, and strictly speaking, this graph can be a *“forrest”*: a collection of trees. Mostly, people
              like to use the term “tree” anyhow.
              |BR|
              However as this chapter is about requirements and quality, and I’m trying to convince you to be
              strict, this footnote seems non-trivial ...
