.. Copyright (C) ALbert Mietus & Sogeti.HT; 2020

.. _demo1:

[Demo 1] A simple calculator
******************************

The specifications are quite trivial ...


The product we need
===================

.. demo:: Simple Calculator
   :ID: CALC1
   :tags: demo1

   For this demo a simple calculator is used. It should work with intergers; and has only a few requirements. See below.

We use this extremely simplistic example as you will agree on its requirements.


Some general requirements, for all  calculators
===============================================

.. req:: Generic Add
   :ID: CALC_ADD
   :links: CALC1;CALC2
   :tags: general

   All calculators should be able to sum two numbers and show the result.

.. req:: Generic Sub
   :ID: CALC_SUB
   :links: CALC1;CALC2
   :tags: general

   All calculators should be able to subtract a number form another number.

.. req:: Generic Multiply
   :ID: CALC_MULT
   :links: CALC1;CALC2
   :tags: general

   All calculators should be able to multiply two numbers.

.. req:: Generic Divide
   :ID: CALC_DIV
   :links: CALC1;CALC2
   :tags: general

   All calculators should be able to divide two numbers.


Add this is how we test it
==========================

As we have defined only general requirements, we only need some generic tests.

.. test:: Basic addition test
   :id: CALC_TEST_ADD_1
   :links: CALC_ADD;CALC2_1000ND
   :tags: general

   Sum two numbers and verify the result is correct.

   By example: Add  ``2`` and ``5`` and check the result is **7**

.. test:: Big  addition test
   :id: CALC_TEST_ADD_2
   :links: CALC_ADD;CALC2_1000ND
   :tags: general

   Add the numbers ``2222`` and ``5555`` and check the result is **7777**

.. test:: Subtract test
   :id: CALC_TEST_SUB_1
   :links: CALC_SUB;CALC2_1000ND
   :tags: general

   Feed two numbers to the calculators, in the right order and verify the result.
   |BR|
   E.g:

   * Subtract ``5`` from ``7`` and check the result is **2**
   * Subtract ``5555`` from ``7777`` and check the result is **2222**

   .. note::

      Here we specify two test in one test-requirement; just to show another style

.. test:: Multiplication test
   :id: CALC_TEST_MULT_1
   :links: CALC_MULT;CALC2_1000ND
   :tags: general

   You get the idea ...



