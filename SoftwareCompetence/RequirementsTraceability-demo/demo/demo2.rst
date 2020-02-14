.. Copyright (C) ALbert Mietus & Sogeti.HT; 2020

.. _demo2:

[CALC2] The exact calculator
****************************

This demo is just a bit more complicated then :ref:`demo1`: this product-variant has *one* extra requirement.

A bit more complicated product
==============================

.. demo:: Exact Calculator
   :ID: CALC2
   :tags: demo2
   :links: CALC1

   This calculator should work with `Fractional Numbers <https://en.wikipedia.org/wiki/Fraction_(mathematics)>`_, and be
   exact for very big numbers; as defined in :need:`CALC2_1000ND`

   .. warning::

      This implies ``floats`` are not possible in the implementation


The extra requirement
=====================

.. spec:: Big fractional numbers
   :id: CALC2_1000ND
   :links: CALC_ADD;CALC_SUB;CALC_MULT;CALC_DIV
   :tags: demo2

   The :need:`CALC2` should work with fractions; where nominator and denominator can be very long: up to **1000
   digits**.

.. _test_hotfix:

Hotfix the missing test
-----------------------

We also *repair* the missing test in demo1, but only for demo2 (Because it is still a *demo!*).

.. test:: DIV test (demo2 only)
   :id: CALC2_TEST_DIV_1
   :links: CALC_DIV; CALC2_1000ND
   :tags: demo2

   Subtract ``1/3`` from ``1/2`` and check the result is **1/6**.

   .. note::

      This test is was intentionally “forgotten” as explained in the :ref:`forgotten test <forgotten_test>`.

      Therefore it is only added for the :need:`CALC2`. See :ref:`the notes about the forgotten
      test<about_forgotten_test>` for more info.

How to test?
============

The :need:`CALC2_1000ND` requirement is a good example of a “*nonfunctional*” (actually: a non-distributable)
specification. It is valid for all other requirements; all parts of the implementation should adhere to it.

Testing this requirement is also different too.  The same tests are valid: we have to add, subtract, multiply and
divide.
|BR|
Only, now we have to use other numbers; really big ones!

Traditionally
-------------

In the traditional world, using the TMAP-terms, this approximately come down to:

* Reuse the *logic test*.
* Change a *physical test* (or add one).

Modern
------

When using an agile test-automation framework this implies

* The ATS (Automated Test Script) isn’t altered.
* Some “Test-Vectors” (or test-data) is added: the big-fractions.

Specification Traceability
--------------------------

To be able to trace some test need to be adapted, we only have to add some “links” between the relevant test and the
additional (test) specification. That is done in :need:`CALC2_1000ND` (possible you have to click/open the see the
details), by adding some (outgoing) links to the existing tests.

.. note::

   The incoming links are added automatically
