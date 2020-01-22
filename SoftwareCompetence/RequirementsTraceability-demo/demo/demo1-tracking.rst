Requirements Traceability, for demo1
====================================

Given all (kind of) specifications that are defined for :need:`CALC1`, we can generate a overview of *needs*:

.. needtable::
   :tags: demo1
   :style: table
   :columns: id;type;title;incoming;outgoing
   :sort: type


Some people prefer to see the same information in a graphical way:

.. needflow::
   :tags: demo1

Summary
--------

This very simple demo has only *one* product with *four* requirements and a few tests. There a no product-variant, no
product-increments (“new releases”) and no intermediate (or hierarchical) specifications. As a (deliberate) result,
**Requirements Traceability** is easy.
|BR|
Everybody will understand that when the product-definition or one of the four requirements will change, the
implementation will (partially) change. And so, some test has to be re-run; given the smallness, just redo all and one
is done.

When we introduce variants, sprint-increments, multiple (sub)components, libraries, versions, releases, etc. the
challenge becomes bigger. Especially when a project-teams grows, its might become a nightmare to know which test has to
be re-run, when a specification changes.

Unless one uses a (simple) approach as shown above. Then, everbody can just see which *rework* is needed when something
“upstream” changes. And, by adding a “status” to each spec, we can even make this visual.

See :doc:`demo2-spec` for a bit more complex example: Adding a product-variant and (only) one extra (non-functional)
requirement. 


