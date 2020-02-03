Requirements Traceability, for demo1
====================================

Given all (kind of) specifications that are defined for :need:`CALC1`, we can generate a overview of *needs*. There are
several ways to show that information; we use 2

The Requirements Matrix (table)
--------------------------------

.. needtable::
   :tags: demo1;general
   :style: table
   :columns: id;type;title;incoming;outgoing
   :sort: type

.. note::

   For now, ignore the *links* to CALC2 and CALC2_1000ND. Those will be in explained in :ref:`demo2`

A graphical view (“tree”)
-------------------------
Some people prefer to see the same information in a graphical way:

.. _demo1_graph:

.. needflow::
   :tags: demo1;general

.. attention::

   .. _forgotten_test:

   The graph (as well as the table) clearly shows there is no tests for :need:`CALC_DIV`. For this demo, it’s
   intentional. Note, however, that --as there are :need_count:`type=='test' and 'general' in tags` tests defined-- one
   can easily oversee this; even in this simple case!


Summary
--------

This very simple demo has only *one* product with *four* requirements and a few tests. There are no product-variant, no
product-increments (“new releases”) and no intermediate (or hierarchical) specifications. As a (deliberate) result, its
**Requirements Traceability** is simple.
|BR|
Everybody can understand the when product-definition --one of the four requirements will change-- the implementation
will (partially) change. And so that, some tests have to be re-run.

Also, a changed requirement(s) and the corresponding test are only one click aways.

Next steps
----------

When we introduce variants, sprint-increments, multiple (sub)components, libraries, versions, releases, etc. the
challenge becomes bigger. Especially when a project-teams grows, its might become a nightmare to know which test has to
be re-run, when a specification changes.

Unless one uses a (simple) approach as shown above. Then, everbody can just see which *rework* is needed when something
“upstream” changes. And, by adding a “status” to each spec, we can even make this visual.

See :ref:`demo2` for a bit more complex example: Adding a product-variant and (only) one extra (non-functional)
requirement.
