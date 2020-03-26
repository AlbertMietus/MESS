.. Copyright (C) ALbert Mietus 2020

.. _about_forgotten_test:



The forgotten test
==================

Intentionally, one test is :ref:`“forgotten” <forgotten_test>` for the first demo. However it is needed and “hot-fixed” for :ref:`the second one <test_hotfix>`.
|BR|
Surely this is not typical in one documentation-release.

Therefor some *tricks* are used to show this in one go. Those tricks are documented here.

By adding some ‘tags’ to the various requirements one can filter on those when generating an overview. And only show the intend ones. This can be useful by-example to labels ‘needs’ for a specific release or product-variant. Here, used a bit more extensive.

Particulars
-----------

As typical each product has it “own” tag: ``demo1`` or ``demo2``. As we have some tests that should be selected on one page, but not on another we use an extra tag: ``general``.
|BR|
Most test-cases are labeled with ``general``, as are the generic requirements. Whereas the “forgotten” test :need:`CALC2_TEST_DIV_1` is labeled ``demo2``

.. code-block:: rst
   :emphasize-lines: 4,11

   .. test:: Basic addition test
      :id: CALC_TEST_ADD_1
      :links: CALC_ADD;CALC2_1000ND
      :tags: general

      Sum two numbers ....

   .. test:: DIV test (demo2 only)
      :id: CALC2_TEST_DIV_1
      :links: CALC_DIV; CALC2_1000ND
      :tags: demo2

      Subtract ...


Now it becomes possible to show the relations with, or without that test.

In the :ref:`first demo <demo1_graph>`, we filter on ‘demo1` and ‘general’. So we get the product, the generic requirements and most tests. But not the forgotten one.

.. code-block:: rst
   :emphasize-lines: 2

   .. needflow::
      :tags: demo1;general

*After* we have “hot-fixed” the test, we can simply select all test for the :ref:`second graph <demo1_graph>`

.. code-block:: rst
   :emphasize-lines: 2

   .. needflow::
      :tags: demo2;general

Actually, we didn’t really “hot fix” it; it was only defined for demo2. But linked to a general requirements.

Normally, you don’t need to use this kind of tricks; it better to not forget a test, or really fix it.
