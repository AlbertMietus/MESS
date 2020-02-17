.. _RT_RTM_CALC2:

The classical Requirements Traceability Matrix
================================================

Most literature about requirements-traceability focus on the Requirements Traceability Matrix [#RTM]_. This table gives the relation between the (high level) requirements versus all test. As ‘needs’ can’t generate this table (yet), I have created one as example.

With this overview one get insight about which test are needed to verify one requirement. Sometimes it explicitly counts the number of available tests pro requirement too. Albeit that is a nice result, the ATM isn’t that useful in an agile environment. When a requirement is added, ore one changes, the RTM itself gives little help to update the table.


.. list-table:: RTM for the :need:`CALC2`
   :class: RTM-rotated-head
   :header-rows: 1
   :widths: 25 15 15 15 15 15

   * - Test\\Req
     - :need:`CALC_ADD`
     - :need:`CALC_SUB`
     - :need:`CALC_MULT`
     - :need:`CALC_DIV`
     - :need:`CALC2_1000ND`
   * - :need:`CALC_TEST_ADD_1`
     - X
     -
     -
     -
     - X
   * - :need:`CALC_TEST_ADD_2`
     - X
     -
     -
     -
     - X
   * - :need:`CALC_TEST_SUB_1`
     -
     - X
     -
     -
     - X
   * - :need:`CALC_TEST_MULT_1`
     -
     -
     - X
     -
     - X
   * - :need:`CALC2_TEST_DIV_1`
     -
     -
     -
     - X
     - X



.. rubric:: Footnotes & Links

.. [#RTM] Often shorthanded to RTM, or simle “Traceability Matrix”, as wikipedia does.

Wikipedia on RTM:
   https://en.wikipedia.org/wiki/Traceability_matrix
