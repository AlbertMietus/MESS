.. Copyright (C) ALbert Mietus & Sogeti.HT; 2020

**********************
Demo: Some calculators
**********************

This chapter contains a few demonstrations of the  Requirements Traceability concept.

We start with a very simple product: the :need:`CALC1`; with only a few generic requirements and tests. By defining
those “needs”[#needs]_ it becomes possible to show a (generated) :ref:`graph <demo1_graph>` with the relations between
them.  |BR| Probably, you will be able to implement and verify this simple product without (formal)
requirements-traceability; but it gives a nice introduction to the concept.


Then, a new product the :need:`CALC2` is defined, in the same way.
|BR|
It has only one (tricky) additional requirement; which makes both implementation and validation (testing) more
defiant. Again, a nice :ref:`graph <demo2_graph>` is shown.

Likewise, we could add more demo’s with more and more specifications, tests and *need* at multiple-levels; but you will
get the idea: By simple ‘defining’ the needs, it becomes possible to get insight; independent of the size of the products
or the numbers of specifications.

Finally, an :ref:`overall graph <all_graph>` is shown, with all the products, all the tests, and all the connecting
*needs*. Just because it is easy to include it; it takes a handful of lines, only


.. toctree::
   :glob:
   :maxdepth: 3

   demo1
   demo1-tracking
   demo2
   demo2-tracking
   TraceAll

.. rubric:: Footnotes & Links

.. [#needs] The universal term ‘*need*’ is used for all kinds of requirements, specifications, test-specs, etc.
            This name comes from the “needs” extension to “sphinx-docs” that we use in this demo.

Needs:
  http://sphinxcontrib-needs.readthedocs.io

Sphinx:
   https://www.sphinx-doc.org/
