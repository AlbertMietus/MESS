Requirements Traceability [Demo 1]
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


Lessons learned
---------------

#. This graph clearly shows there are **no tests** for :need:`CALC_DIV`. This is easily overseen as there are four
   requirements *and* four tests defined.
#. When the requirement :need:`CALC_ADD` changes, two tests might need an update.
#. Likewise, for the other requirements, it is directly visual where the relations are.

.. attention::

   .. _forgotten_test:

   The “forgotten test” is intentional in this first demo.  It will be fixed in the :ref:`next chapter<test_hotfix>`,
   and you will see it in the other graphs.

   Therefore I had to use some “trick” in needs; see :ref:`the notes about the forgotten test<about_forgotten_test>` for
   more info.


The Requirements Matrix (table)
===============================

Some people prefer to see the same information in a table; again this one is automatically generated.

.. needtable::
   :tags: demo1;general
   :style: table
   :columns: id;type;title;incoming;outgoing
   :sort: type

.. hint::

   For now, ignore the *links* to CALC2 and CALC2_1000ND. Those will be in explained in :ref:`demo2`

Lessons learned
---------------

#. This generated tabular overview kind of act as an index to all “clickable” *needs* It a great page to bookmark.
#. One can even add a status-column (not shown here), or filter on (show only) e.g. test that fails.
#. It gives less insight; therefore it good to have both overviews.


Summary
=======

This very simple demo has only *one* product with *four* requirements and a few tests. There are no product-variant, no
product-increments (“new releases”) and no intermediate (or hierarchical) specifications. As a (deliberate) result, its
**Requirements Traceability** is simple.
|BR|
Everybody can understand that when product-definition --one of the four requirements-- will change, the implementation
will (partially) change. And so that, some tests have to be re-run.

Also, a changed requirement(s) and the corresponding test are only one click away.

Next steps
----------

When we introduce variants, sprint-increments, multiple (sub)components, libraries, versions, releases, etc, the
challenge becomes bigger. Especially when a project-teams grows, it might become a nightmare to know which test has to
be re-run, when a specification changes.

Unless one uses a (simple) approach as shown above. Then, everybody can just see which *rework* is needed when something
“upstream” changes. And, by adding a “status” to each spec, we can even make this visual.

See :ref:`demo2` for a bit more complex example: Adding a product-variant and (only) one extra (non-functional)
requirement.
