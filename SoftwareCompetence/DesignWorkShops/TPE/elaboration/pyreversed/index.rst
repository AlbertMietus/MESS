.. Copyright (C) 2020: ALbert Mietus.

.. _TPE_pyreversed_classes:

=========================
Pyreversed class diagrams
=========================

Extracting class diagrams from code is easy; there exist many tools. For python ``pyreversed`` is the most used one.

The readability of the diagram is strongly depended on the tool, the selected options, and mostly: the **quality** of
the design/code. Do not expect nice diagrams, when somebody created the code without a proper design!

concurrent.futures.thread.ThreadPoolExecutor
============================================

The class-diagrams below are automatically generated; using `pyreverse`.
Two analyses are made:

* Showing all details (right)
* Showing only the “public” parts

.. list-table::
   :header-rows: 1

   * - PUB_ONLY (DEFAULT)
     - ALL
   * - .. figure:: ./concurrent.futures.thread/ThreadPoolExecutor-f_PUB_ONLY.svg
     - .. figure:: ./concurrent.futures.thread/ThreadPoolExecutor-f_ALL.svg


Questionnaire
=============

#. Which of the two diagrams are the most useful?
#. How *bad* (iff at all) are “to many details”?
#. Which details should not be inclused? (when you do the analyse manually)



----------


.. seealso::

   Docs
    * https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
    * https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future

   Code
     * https://github.com/python/cpython/blob/master/Lib/concurrent/futures/thread.py
     * https://github.com/python/cpython/blob/master/Lib/concurrent/futures/_base.py

   Version
      The Python3.4.1 code is used to geneate the diagrams above.
