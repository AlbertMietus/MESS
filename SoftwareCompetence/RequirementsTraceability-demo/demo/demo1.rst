.. Copyright (C) ALbert Mietus & Sogeti.HT; 2020

.. _demo1:

[Demo 1] The Simple Calculator
******************************

The specifications are quite trivial ...


The product we need
===================

.. demo:: Simple Calculator
   :ID: CALC1
   :tags: demo1

   In this demo, a simple calculator should be designed. It should work with intergers; with a maximal length of 8 digits,

   We use a very simple example, as you probably understand the specifications even with spending a lot of text on it.

Some general requirements, for all  calculators
===============================================

.. req:: Simple Add
   :ID: CALC_ADD
   :links: CALC1;CALC2
   :tags: general

   All calculators should be able to sum two numbers and show the result.

.. req:: Simple Sub
   :ID: CALC_SUB
   :links: CALC1;CALC2
   :tags: general

   All calculators should be able to subtract a number form another number.

.. req:: Simple Multiply
   :ID: CALC_MULT
   :links: CALC1;CALC2
   :tags: general

   All calculators should be able to multiply two numbers.

.. req:: Simple Divide
   :ID: CALC_DIV
   :links: CALC1;CALC2
   :tags: general

   All calculators should be able to divide two numbers.

Add this is how we test it
==========================

As we have defined only general requirements, we only need some generic tests.

.. test:: Basic Simple Addition test
   :id: CALC_TEST_ADD_1
   :links: CALC_ADD;CALC2_1000ND
   :tags: general

   Add the numbers ``2`` and ``5`` and check the result is **7**

.. test:: Advanced Simple Addition test
   :id: CALC_TEST_ADD_2
   :links: CALC_ADD;CALC2_1000ND
   :tags: general

   Add the numbers ``2222`` and ``5555`` and check the result is **7777**

.. test:: A  Simple Subtract test
   :id: CALC_TEST_SUB_1
   :links: CALC_SUB;CALC2_1000ND
   :tags: general

   * Subtract ``5`` from ``7`` and check the result is **2**
   * Subtract ``5555`` from ``7777`` and check the result is **2222**

   Here we specify two test in one test-requirement; just to show another style

.. test::  Simple Multiplication test
   :id: CALC_TEST_MULT_1
   :links: CALC_MULT;CALC2_1000ND
   :tags: general

   You get the idea ...



