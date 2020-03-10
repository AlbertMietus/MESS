.. Copyright (C) 2020: ALbert Mietus.

Design Analyse
==============

In this second part of the workshop, we are going to study the **design** of the TPE.

Designing a TPE is (too) complex; that is not within the scope of this :ref:`DesignWorkShops`. Though understanding the
design is...
|BR|
A great (embedded) Software Designer should be able to extract the design from the existing code, even when it is
undocumented and badly described. Especially then, your skills are vital.

So, let us practice them.

You are going to create “the” design of the python-implementation of the TPE. Both the static and dynamic
(behavioural) UML-diagrams are needed.

.. note::

   * This exercise is *not* about the cleanness of the UML-diagrams; it about the design itself.
   * Use a “whiteboard” to make the designs, not a fancy tool! When coworkers do understand it will do!
   * Optionally, you can eventually (later!) draw them nicely in plantUML.

.. toctree::

   static
   dynamic

.. tip:: WoW

   1. Use the (latest) Python-3 code; it quite good readable; eve when you are not a python-expert

      * Take the simplified (conceptual): ref: `TPE_API` as a starting point; additional functionality that
        the real code included does not have to be included. Of course essential things must
        being described. The choice of "essential" is yours.

      * You may use the documentation of all classes that used; when needed.

   2. Start with a short quick analyse, make notes and try to understand it. Then continue with other parts of the
      analyse and repeat.

      * Don’t use “UML-tool” in the first few steps; possible not even UML-diagrams.
      * Simplify the code (on a whiteboard), use lines & arrows to show values (parameters, key-variable, ect) are
        *passed around*.
      * Guess the important parts, like “somewhere the return values should be stored”, and “where are the threads
        created”; and make sure the are on that sketch

   3. Summary all in (draft) UML diagrams. Check it is complete and not to detailed

      * Remove all details from the design, that aren’t essential to the design itself. And a part of the freedom to implement it (the programmmer)


.. admonition:: Done?

   Show this *minimal design* to a peer-group. And ask them to explain the design.

   * You are not allowed to explain it, nor to answer questions!
   * Whenever there are questions, there are unclear parts!
     |BR|
     Then you should know: You have to improve your design!


