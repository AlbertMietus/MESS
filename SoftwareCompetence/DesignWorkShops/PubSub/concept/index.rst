.. Copyright (C) 2020: ALbert Mietus.

Introduction
============

An almost trivial example of PubSub is the daily newspaper:

 Once you get an subscription, you automatically get each new publication.

Typically, your are not the only one. The *same* ‘newspaper’ is send to all subscribers: everybody got his own
*copy*. And, when somebody cancels his subscription all others still het there daily update.
|BR|
Also notice: your copy is undependent of that the neighbours. And, until you subscribe, the publisher does not know
you.

In software-engineering we call that **uncoupled** or *loosely coupled*; and that is great.


.. uml:: PubSub-newspaper.puml

.. toctree::
   :maxdepth: 2

   advantages
   Use
   API
