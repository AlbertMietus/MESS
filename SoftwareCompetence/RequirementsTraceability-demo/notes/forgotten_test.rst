.. Copyright (C) ALbert Mietus 2020

.. _about_forgotten_test:



The forgotten test
==================

Intentionally, one test is :ref:`“forgotten” <forgotten_test>` for the first demo. It is needed for the second one; as explained in :ref:`test_hotfix`.
|BR|
Surely this is not typical in one documentation-release. Some *tricks* are used to show this in one go. Those tricks are documented here.

This is done by adding some ‘tags’ to the various requirements, and filtering on those tags to show only the intend ones. For normal use, you can ignore those tags.

Particulars
-----------

As typical, each product has it “own” tag: ``demo1`` or ``demo2``. Such a tag can be added to each need, and be used to filter when generating overviews.

As we have some tests that should be selected on one page, but not on another we use an extra tag: ``general``.
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
