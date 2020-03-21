.. Copyright (C) 2020: ALbert Mietus.

.. _PubSub_use:

===
Use
===

As typical with *Design Patterns* there are many ways to implement it. Here we focus on the “Topic” approach. It
decouples modules by defining a generic interface and act as a kind of “man-in-the-middle”.

Both the ``Publisher`` and the ``Subscribers`` share a common :class:`~pubsub.Topic` instance::

  from pubsub import Topic
  t = Topic("Just a demo")


Publishers
==========

Publishing a value is very simple; assuming ``t`` is a :class:`pubsub.Topic` instance::

  t.publish("Hello World")


Subscribers
===========

Each subscriber should register a ``callback``, which will be called “automagical” when a new value is available::

  t.subscribe(demo_cb)

Where ``t`` is topic (an instance of :class:`pubsub.Topic`) and ``demo_cb`` is the *callback*. This can a function or other
kind of callable. Multiple subscriptions are possible, by registering another::

  t.subscribe(demo_oo_cb)

.. _PubSub_callback_demo:

callbacks
---------

A callback is a callable, that should process the new value. Basically, it is just a function (or method) with the
correct signature. A trivial example is::

  def demo_cb(value, topic):
     print("Function-Demo:: Topic: %s has got the value: %s" %(topic, value))

It can also be a method, when you prefer an OO-style::

  class Demo:

    def demo_oo_cb(self, val, topic):
        print("Method-demo: I (%s) got '%s' from topic %s" %(self, val, topic))

.. seealso::

   * :class:`pubsub.AbstractType.Publisher`
   * :class:`pubsub.AbstractType.Subscriber`
   * :ref:`CallBack Signature <PubSub_callback_signature>`
