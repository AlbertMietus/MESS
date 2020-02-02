.. Copyright (C) ALbert Mietus & Sogeti.HT; 2020

.. _demo2:

The Exact Calculator (Demo 2)
******************************

This demo is just a bit more complex as :ref:`demo1`; it just add a product-variant with *one* extra requirement.

Specifications
==============

.. demo:: Exact Calculator
   :ID: CALC2
   :tags: demo2
   :links: CALC1

   This calculator should work with `Fractional Numbers <https://en.wikipedia.org/wiki/Fraction_(mathematics)>`_ and be
   exact (and able to show/process) for very big numbers; as defined in :need:`CALC2_1000ND`

   .. warning::

      This implies, ``floats`` are not possible in the implementation


The extra requirement
---------------------

.. spec:: Fraction
   :id: CALC2_1000ND
   :links: CALC_ADD;CALC_SUB;CALC_MULT;CALC_DIV
   :tags: demo2

   The :need:`CALC2` should work with fractions; where nominator and denominator can be long: 1000 digits

HotFixing the missing test
--------------------------

We also *repair* the missing test in demo1, but only for demo2 (Because its a demo ....)

.. test:: DIV test (demo2 only)
   :id: CALC2_TEST_DIV_1
   :links: CALC_DIV; CALC2_1000ND
   :tags: demo2

    .. note::

       Intentional added only for demo2 :ref:`CALC2`

Demo Notes
==========

In this demo some *tricks* are used; like the fixing a missing test :need:`CALC2_TEST_DIV_1`, and combining some
requirements for demo1 (:need:`CALC1`) and demo2 (:need:`CALC2`).

Therefore the ``:tags:`` `general`, `calc1` and `calc2` are used in the ``req::` and ``:spec`` *directives*, to be
able to filer them in the tables and graphs.  
