Requirements Traceability [CALC2]
*********************************

As in “:doc:`demo1`”, we can automatically generate the an overview of the requirements.

The tree view
=============

.. _demo2_graph:

.. needflow::
   :tags: demo2;general

Lessons learned
---------------

#. We can directly see that specification :need:`CALC2_1000ND` influences all existing test-cases.
#. Each test *depends* on both a (functional) requirement and a (non-functional) specification (at least in this case).
#. The requirements-relations can become more complicated, even by adding **only** *one* requirement!

Can you imagine what will happen when we add a handful of requirements to the calculator (*memory*, *square-root*,
*powers*)? Or, a few more non-functionals (*speed-of-operation*, *floats*). Then the complexity quickly raises even for
such a simple product.  And it becomes hard to predict which tests have to be adapted or rerun.

Likewise, when a few requirements become altered in an upcoming sprint: can you predict which tests will have to change?
A graph, as above, will certainly help in working that out.


The table view
==============

.. needtable::
   :tags: demo2,general
   :style: table
   :columns: id;type;title;incoming;outgoing
   :sort: type


Lessons learned
---------------

#. The advantage of a table-view is that is will only grow in one direction: it just becomes a bit longer.
#. Even for a big project, it’s a great page to bookmark and use as a start-page for all kinds of requirements.
   |BR|
   Probably, you like to split it into the kind of ‘need’.

It would be great to show a classical `Requirements Traceability matrix
<https://en.wikipedia.org/wiki/Traceability_matrix>`_ (RTM) too. This table shows the relations between all the
requirements and all the tests.

.. note::

   As ‘needs’ currently does not support classical *RTM*\s, I can’t generate/show it here.  See :ref:`a manually made
   TRM <RT_RTM_CALC2>` to get the idea. As you will see: it’s easy to read.
   |BR|
   However, its quite hard to grasp deep relations; then the tree above is more helpfull.

Next steps
==========

We might add more product-variants, or more sprints to convince you that requirement-traceability is important. The only
effect is more pages with (trivial) requirements, specifications or other ‘needs’. And the same to generated overviews;
the later cost only a small number of lines, independent of the size of the product. So we will leave that as an
exercise.

As a bonus, we will show you one more generated graph: :ref:`all_graph`, combining the :need:`CALC1` and :need:`CALC2`
requirements.

Whenever you have more quistions, you can email me :sogeti-email:`Albert.Mietus`.


