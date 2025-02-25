Requirements Traceability [CALC1]
**********************************

With the defined ‘needs’, their relations can be shown automatically, or some tables with relevant ones can be
listed. Below you will find two examples, for :need:`CALC1`.

.. _demo1_graph:

A graphical view (“tree”)
=========================

This view shows the relationship between all kinds of specifications. It is fully automatically generated and will be
updated when the specifications change.

.. needflow::
   :tags: demo1;general
   :filter: 'RequirementsTraceability' in project 


Lessons learned
---------------

#. This graph clearly shows there are **no tests** for :need:`CALC_DIV`. This is easily overseen as there are four
   requirements *and* four tests defined.
#. When the requirement :need:`CALC_ADD` changes, two tests might need an update.
#. Likewise, for the other requirements, it is directly visual where the relations are.

This very simple demo has only *one* product with *four* requirements and a few tests. There are no product-variant, no
product-increments (“new releases”) and no intermediate (or hierarchical) specifications. As a (deliberate) result, its
**Requirements Traceability** is simple.
|BR|
Still, its easy to forget a test; as I did. Did you noticed it?

.. attention::


   The “forgotten test” is intentional in this first demo.  It will be hot-fixed in the :ref:`next
   chapter<test_hotfix>`, and you will see it in the other graphs.

   Therefore I had to use some “trick” in needs;

   .. seealso:: :ref:`the notes about the forgotten test <forgotten_test>` for more info.


The Requirements Matrix (table)
===============================

Some people prefer to see the same information in a table; again this one is automatically generated.

.. needtable::
   :tags: demo1;general
   :style: table
   :columns: id;type;title;incoming;outgoing
   :sort: type
   :filter: 'RequirementsTraceability' in project

.. hint::

   For now, ignore the *links* to CALC2 and CALC2_1000ND. Those will be in documented in :ref:`demo2`

Lessons learned
---------------

#. This generated tabular overview kind of act as an index to all “clickable” *needs*. It’s a great page to bookmark.
#. One can even add a status-column (not shown here), or filter on (show only) e.g. test that fails.
#. It gives less insight; therefore it good to have both overviews.


Everybody understands that when the product-definition changes, the implementation will change too. And, that the
test-set will change, partially; by example: new tests will be added.
|BR|
However, some tests may even become obsolete!

So, just re-running all (existing) tests as a regression-test, may not work. The question is: which of all test are
related to the changed requirement?

With a table as above, the answer is just one click away.


Next steps
==========

When we introduce variants, sprint-increments, multiple (sub)components, libraries, versions, releases, etc, the
challenge becomes bigger. Especially when a project-teams grows, it might become a nightmare to know which test has to
be re-run, when a specification changes.

Unless one uses a (simple) approach as shown above. Then, everybody can just see which *rework* is needed when something
“upstream” changes. And, by adding a “status” to each spec, we can even make this visual.

See :ref:`demo2` for a bit more complex example: Adding a product-variant and (only) one extra (non-functional)
requirement.
