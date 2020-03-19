.. Copyright (C) 2020: ALbert Mietus.

.. _PubSub:

=============
**Pub**/*Sub*
=============

.. sidebar:: **HighTech** vs *Gooogling*

   When you search for `Pub/Sub`, you will find over 312M hits! Mostly about cloud-computing, and on how servers exchange
   messages via a *‘broker’*.
   |BR|
   Often it is infrastructure engenering based.

   This workshop isn’t about that. We focus on *Modern, Embedded Software Systems*: How can an (HighTech) Software Engineer use
   this pattern to create better software.


.. post:: 		
   :tags: DesignWorkShops
   :category: practice
   :location: ehv
   :language: en

   :practice-time: 2 * 1 hour

   The publish-subscribe *architecture*-**pattern** is very popular to route messages, according to `WikiPedia
   <https://en.wikipedia.org/wiki/Publish–subscribe_pattern>`_.  It is used much more generic, however. This workshop shows how
   to use it in an embedded application; or another single process application.
   |BR|
   Then it becomes a HighTech (embedded) software **design pattern**.

   We start with a simple implementation of **Pub**/*Sub*. You can experiment with that (Python) code and/or port it to your
   favorite language. Then, you are asked to **design** a cached, distributed version. Which is a bit more ambitious. And even
   though the result is probably *pointless*, it’s a great Design-Exercise and a lot of fun!

   It will help you to understand Pub/Sub, help you to use it in embedded software. Eventually, you may need Pub/Sub in a
   distributed environment. Then, it is better to use one of the existing ones, like `DDS
   <https://en.wikipedia.org/wiki/Data_Distribution_Service>`_ (Data Distribution Service); which more efficient and even
   RealTime!
   |BR|
   But, by knowing how to implement it and are able to design it, will help you to use it for the better



.. toctree::
   :glob:

   *
   */index



------------------------


.. _PubSub_links:

.. seealso::

   * ...
