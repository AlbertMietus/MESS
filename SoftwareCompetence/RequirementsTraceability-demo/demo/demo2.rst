The Exact Calculator (Demo 2)
*****************************

This demo is just a bit more complex as :doc:`demo1`; it just add a product-variant with *one* extra requirement.

Specifications
==============

.. demo:: Exact Calculator
   :ID: CALC2
   :tags: demo2

   This calculator should work with `Fractional Numbers <https://en.wikipedia.org/wiki/Fraction_(mathematics)>`_ and be
   exact (and able to show/process) for very big numbers.


   All requirements for :need:`CACL1` are also valid for this product-variant.

.. warning::

   This implies, ``floats`` are not possible in the implementation


The extra requirement
---------------------

.. req:: Fraction
   :id: CALC2_1000ND
   :tags: demo2

   The :need:`CALC2` should work with fractions; where nominator and denominator can be long: 1000 digits
