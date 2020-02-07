.. Copyright (C) ALbert Mietus & Sogeti.HT; 2020

==============================
Requirements Traceability Demo
==============================

.. post:: 2020/02/02
   :tags:
   :category:
   :location: Eindhoven
   :language: en

   Requirement-Management, and especially *“Tracking Requirements”* isn’t that complicated; but it needs some discipline.
   Often that discipline is “replaced” by a tool, which is encouraged by tool-vendors. That hardly ever works.

   This chapter introduces requirements traceability in a conceptual, but pragmatic way. Its shows what a team has to do
   (defining requirements and describing the relations) and what the benefit is. It assume a (more of less) agile
   way-of-work, and shows how ti can becomes lean. A small investment in good requirements definitions make validations
   a lot easier.

   And yes, it used a tool: a free one: A simple way to write maintainable documentation, including all
   requirements. With a plugin that can visualize all specifications and their relations.

.. admonition:: Summary (testers view)

   .. image:: ./V-IdeaWorkProduct-alfa.png
      :width: 33%
      :align: right

   * For a simple development cycle, it easy to trace the validation the product:
     *All features should be covered by a test, and all should pass*.
   * When multiple products --or multiple releases-- are mandatory, this becomes quickly ambiguous:
     *Some test have to pass and only the essential specifications needs test-cases.*
   * Then ‘requirements traceability’ becomes crucial:
     **It gives insight in which ‘specs’ are required by each product/release and which tests are essential.**
   * This article (as part of a workshop) shows a down-to-earth demo how you set-up the ‘requirements traceability’ and
     how to use it.
   * We use the ‘tester view’: Be able to demonstrate the *product* **does** what was *aimed for*!


.. separate admon from quote
..


   “Requirements traceability is a sub-discipline of requirements management within software development and systems
   engineering ...”

   “... is defined as "the ability to describe and follow the life of a requirement in both a forwards and backwards direction”

   --- https://en.wikipedia.org/wiki/Requirements_traceability


.. rubric:: Content
.. toctree::
   :maxdepth: 2

   goal/index
   demo/index
   notes/index


More info? Contact Albert: :sogeti-email:`Albert.Mietus`; +31 (0)6 526 592 60. Or use the comment section below.
