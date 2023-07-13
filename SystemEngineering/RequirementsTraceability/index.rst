.. Copyright (C) ALbert Mietus & Sogeti.HT; 2020

.. _RequirementsTraceability:

=========================
Requirements Traceability
=========================

.. post:: 2020/02/15
   :tags: SysEng
   :category: lecture 
   :location: Vianen 
   :language: en 

   :study-time: 1 hour

   Requirement-Management, and especially *“Tracking Requirements”* isn’t that complicated, but it needs some
   discipline.  Often that discipline is *replaced* by a tool, which is encouraged by tool-vendors. That hardly ever
   works.

   This blog introduces requirements traceability in a conceptual, but pragmatic way. It shows :ref:`--as a
   demo--<RT_demo>` what a team has to do (defining requirements and describing the relations) and what the benefit
   is. It assumes a (more or less) agile way-of-work and shows how it can become lean. A small investment in good
   requirements definitions makes validations a lot easier.

   And yes, it used a tool: a free one; as part of the documentation-system that is used for this side.  An structured,
   version-controllable, textual way to write documentation, including all requirements. With a plugin that
   can visualize all specifications and their relations.
   |BR|
   Those *“particulars”* will be shown too.

.. admonition:: Summary (testers view)

   .. image:: ./V-IdeaWorkProduct-alfa.png
      :width: 33%
      :align: right

   * For a simple development cycle, it easy to trace the validation of the product:
     *All features should be covered by a test, and all should pass*.
   * When multiple products --or multiple releases-- are mandatory, this becomes quickly ambiguous:
     *Some tests have to pass, and only the essential specifications need test-cases.*
   * Then ‘requirements traceability’ becomes crucial:
     **It gives insight into which ‘specs’ are required by each product/release and which tests are essential.**
   * This article (as part of a workshop) shows a down-to-earth demo of how you set-up the ‘requirements traceability’
     and how to use it.
   * We use the ‘tester view’: Be able to demonstrate the *product* **does** what was *aimed for*!

.. rubric:: Content
.. toctree::
   :maxdepth: 2

   goal/index
   demo/index
   notes/index


More info? Contact Albert: :sogeti-email:`Albert.Mietus`; +31 (0)6 526 592 60. Or use the comment section below.
