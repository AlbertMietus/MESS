.. Copyright (C) 2020: ALbert Mietus.

========
Practice
========

This last section of this :ref:`PubSub` workshop is short. It only contain some practice (ideas). Two are on practicing
your design skills, the other two are more coding-oriented.


Design Analyse
==============

Given the python implementation, including the shown “Use-Cases”: Analyse the design in detail:

1. Make a (quick) static design-analyse.

   Resulting in some package- and class- diagrams.

2. Make a (draft) dynamic design-analyse.

   At least a sequence-diagram for each of the “use-cases”

Port to C/C++
--------------

3. Can you port (or re-implement) the python examples to C/C++?

   Surely, you have to change some details; as a generic data-type (“value”) is not available. It is fine, to use a
   *string-type*. And just “print” it in the demo-callbacks (like I did).

Design a cached, distributed one
================================

The shown (conceptional) implementation works for a single process; optional with threads. In this exercise, you are
going to extent that for “network use”; although it will be a simple, conceptional one. Many existing protocols and
frameworks do exist already! The goal is *not* to challenge them, nor to *use* them.

The goal is to practice your design skills!
|BR|
So, this is a (fun) design-exercise. You should be able to make a (full, conceptional) design in about an hour. That does
imply many fancy options should be left-out:-)

4. Extent the current interface to allow pub/sub between multiple processes; optionally running on multiple computers
   (on the same network).

   * The current API (:class:`~pubsub.Topic`, :meth:`~pubsub.Topic.publish` & :meth:`~pubsub.Topic.subscribe`) are not
     allowed to change. Adding parameters to the class initiation (“the constructor” in C++) is allowed. Adding extra
     methods is also allowed (but see below!).

   * All existing Use-Cases **should** keep working (both the shown one, as many others).

     * The main methods (:meth:`~pubsub.Topic.publish` & :meth:`~pubsub.Topic.subscribe`) should remain exactly the
       same. No more parameters!

     * The default behavior should be “local” (not distributed).

   * There is no requirement for performance. But it is expected that a second “network-get” will be resolved
     locally. So, use a cache to minimize networking

   * The networking should use standard TCP/IP networking (“sockets”). No other network libraries/frameworks are
     allowed.

     * A simple “serialise” will do. Assume, all computers/processes use the same endianness and other encodings.
       |BR|
       Again, use “strings” (only); then this part is easy.

.. hint:: `Deamon <https://en.wikipedia.org/wiki/Daemon_(computing)>`_ &  `lib <https://en.wikipedia.org/wiki/Library_(computing)>`_

   An easy way to design this is to foresee *one* processes handle all the administration (the core of
   :class:`~pubsub.Topic`); including “calling” all the callbacks.
   |BR|
   This is typically called a **daemon**, or *services* on Windows.

   To hide all the networking stuff, arrange a (small) library, that acts as `facade <https://en.wikipedia.org/wiki/Facade_pattern>`_
   and provides the (extended) :ref:`PubSub_API`.


Implement it
------------

5. To check your design above is great, now implement it.

   Or better: implement the design of you co-trainee, and ask him to implement yours!

Remember, a design is a communication-tool: A great design contains exactly those details that your coworker needs to
implement is as it is meant to be, but no more. (S)He should have some freedom to optimize implementation-details.
