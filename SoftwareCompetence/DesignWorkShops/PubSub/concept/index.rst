.. Copyright (C) 2020: ALbert Mietus.

Introduction
============

An almost trivial example of PubSub is the daily newspaper:

 Once you have a subscription, you automatically get each new publication.

Typically, you are not the only subscriber; the *same* ‘newspaper’ is sent to all subscribers: everybody got his
*copy*. And, whenever somebody cancels his subscription, all others still get there update daily.
|BR|
Also notice: your copy is independent of that the neighbors. And, until you subscribe, the publisher does not know
you.

In software-engineering, we call that **uncoupled** or *loosely coupled*, and that is great.
|BR|
As we will explain in the next page.


.. uml:: PubSub-newspaper.puml

.. toctree::
   :maxdepth: 2

   advantages
   Use
   API
