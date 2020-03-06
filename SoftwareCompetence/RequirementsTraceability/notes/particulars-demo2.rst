.. Copyright (C) ALbert Mietus  2020

.. _RT_Particulars_demo2:

======================
 Particulars for CALC2
======================

.. hint::

   Again, you can skip the **particulars** passage when you have no curiosity in the technicalities of ‘needs’ itself.


Describing requirements
=======================

The describing text of any requirement (in ‘needs’) is standard **rst** *(reStructuredText)*. So it can use hyperlinks,
forward-references to other needs and even warning-admonitions.
|BR|
The full textual definition of :need:`CALC2` is:

.. code-block:: rst
   :emphasize-lines: 6-7, 9-11

   .. demo:: Exact Calculator
      :ID: CALC2
      :tags: demo2
      :links: CALC1

      This calculator should work with `Fractional Numbers <https://en.wikipedia.org/wiki/Fraction_(mathematics)>`_, and be
      exact for very big numbers; as defined in :need:`CALC2_1000ND`

      .. warning::

         This implies ``floats`` are not possible in the implementation


The added specification
=======================

Like all other ‘needs’, the specification for :need:`CALC2_1000ND` is straightforward. It links to “earlier”
requirements.

.. code-block:: rst
   :emphasize-lines: 3

   .. spec:: Big fractional numbers
      :id: CALC2_1000ND
      :links: CALC_ADD;CALC_SUB;CALC_MULT;CALC_DIV
      :tags: demo2

      The :need:`CALC2` ...

.. tip::

   * There is no *prescribed* order how the individual ‘needs’ can be linked. It kind of feels more natural to link to
     “higher level” (in the V-model) ‘needs’, and to one that are described “earlier” (in project-time). But when you
     can link them in any order.

   * Similar, a ‘need’ can link to any other ‘need’, independent of its type.
     |BR|
     Above we have used a `spec`, to add this requirement; but a normal `req` (requirement) is possible too. You can
     configure any kind of ‘needs’, as you like.

   * You can even *export* ‘needs’ in one document and *import* them in another. For big projects with many levels of
     modules, and so, specification-documents, this is typical behaviour. In this small calculator example tha is not
     used.

Tracing relations
=================

To be able to trace whetter some test need to be adapted, we only have to add some “links” between the relevant test and the
additional (test) specification.

In :need:`CALC2_1000ND` that is done by adding some (outgoing) links to the existing tests. You may have to open/click the see the details row. 

.. note::

   The incoming links are added automatically.

Inheriting links
----------------

Currently, there is no *inherit option*, One can’t specify that the requirements for `CALC1` are also valid for
`CALC2`.

* By linking the two ``Demonstrators`` we get (almost) the same.
* Alternatively, you can just add the links manually.
* *(or you can use the export/import option and a simple script to modify the json file)*

.. tip::

   As ‘needs’ is an actively maintained open-source project, ‘inheriting’ may be added in a next release.
   |BR|
   Even by you:-)

The hotfix
==========

See :ref:`the notes about the forgotten test<about_forgotten_test>` for the particulars on how to :ref:`forget
<forgotten_test>` and :ref:`add <test_hotfix>` a test in one document.

