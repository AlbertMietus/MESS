.. Copyright (C) ALbert Mietus  2020

.. _RT_Particulars_demo1:

=====================
Particulars for CALC1
=====================

.. hint::

   You should skip the particulars passages, when you not interested in the technical details of this particular tool.


A product (start of the V)
==========================

To define the :need:`CALC1` product the following is described:

.. code-block:: rst

   .. demo:: Simple Calculator
      :ID: CALC1

      For this demo ...

You can see this product has the ID ``CALC1`` and some text. No links are needed, they will be added automatically by
requirements, which are described “later”.


With requirements (one step down into the V)
--------------------------------------------

The requirement :need:`CALC_ADD` has an ID too, and a link to the products it is valid for; here `CALC1` and `CALC2`.

.. code-block:: rst
   :emphasize-lines: 2,3

   .. req:: Generic Add
      :ID: CALC_ADD
      :links: CALC1;CALC2

      All calculators ... able to sum ...

All requirements are described in the same way, as well as each individual requirement can be linked to one or more
products (or product-variants). As this demo has (already) two products, and this requirement is valid for both; you see
them listed here.


And tests (the other side of the V)
-----------------------------------

A test (-case) is also a ‘need’. It is defined in the same approach: a title, an ID and the links to all requirements that
are tested by this one. Here, that is only `CALC_ADD`.

.. code-block:: rst
   :emphasize-lines: 2

   .. test:: Basic addition test
      :id: CALC_TEST_ADD_1
      :links: CALC_ADD

      Sum two numbers and verify ...

Again, the same construction is repeated for all tests.


Tracing the requirements
========================

Generaring the “requirements tree” as displayed :ref:`here <demo1_graph>` is very easy:

.. code-block:: rst
   :emphasize-lines: 1

   .. needflow::
      :tags: demo1;general

Likewise is showing the table overview:

.. code-block:: rst
   :emphasize-lines: 1

   .. needtable::
      :tags: demo1;general
      :style: table
      :columns: id;type;title;incoming;outgoing
      :sort: type


See the documentations of needs (https://sphinxcontrib-needs.readthedocs.io) for details on all options.
