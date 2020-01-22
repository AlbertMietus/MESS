Demo 1: Specifications
======================

This is the basic idea ...

The product we need
-------------------

.. demo:: Simple Calculator
   :ID: CALC1
   :tags: demo1

   In this demo, a simple calculator should be designed.

   We use a very simple example, as you probally understand the specifications even with spending a lot of text on it

The requirements, for the simple calculator
-------------------------------------------

.. req:: Simple Add
   :ID: CALC1_ADD
   :links: CALC1
   :tags: demo1

   The :need:`CALC1` should be able to sum two numbers and show the result.

.. req:: Simple Sub
   :ID: CALC1_SUB
   :links: CALC1
   :tags: demo1

   The :need:`CALC1` should be able to subtract a number form another number.

.. req:: Simple Multiply
   :ID: CALC1_MULT
   :links: CALC1
   :tags: demo1

   The :need:`CALC1` should be able to multiply two numbers.

.. req:: Simple Divide
   :ID: CALC1_DIV
   :links: CALC1
   :tags: demo1

   The :need:`CALC1` should be able to divide two numbers.

Add this is how we test it
--------------------------

.. test:: Basic Simple Addition test
   :id: CALC1_TEST_ADD_1
   :links: CALC1_ADD
   :tags: demo1

   Add the numbers ``2`` and ``5`` and check the result is **7**

.. test:: Advanced Simple Addition test
   :id: CALC1_TEST_ADD_2
   :links: CALC1_ADD
   :tags: demo1

   Add the numbers ``2222`` and ``5555`` and check the result is **7777**

.. test:: A  Simple Subtract test
   :id: CALC1_TEST_SUB_1
   :links: CALC1_ADD
   :tags: demo1

   * Subtract ``5`` from ``7`` and check the result is **2**
   * Subtract ``5555`` from ``7777`` and check the result is **2222**

   Here we specify two test in one test-requirement; just to show another style

.. test::  Simple Multiplication tes
   :id: CALC1_TEST_MULT
   :links: CALC1_MULT
   :tags: demo1

   You get the idea ...
