.. Copyright (C) 2020: ALbert Mietus.

.. _PubSub_API:

===============
The Pub/Sub API
===============

This is the API (and implementation) of a simple :class:`~pubsub.Topic` class; as used in :ref:`PubSub_Use`.

Topic
=====

.. currentmodule:: pubsub

.. class:: Topic

   A :class:`~pubsub.Topic` is like a channel to distribute information (events), in a **Pub**/*Sub* environment.

   This will decouple the :class:`pubsub.AbstractType.Publisher` from the :class:`pubsub.AbstractType.Subscriber` (in
   both directions).

   * On one side is a ``Publisher`` that provides ‘data’ (**value**’s, *events*, ...).
   * The other side has ``Subscribers`` who subscribe to the topic (with **callbacks**).
   * Both ``Publisher`` and ``Subscriber`` are abstract types; there is no concrete class (needed).
   * Any module that calls :meth:`publish` is called a ``Publisher``; likewise, a ``Subscriber`` is anyone calling
     :meth:`subscribe`.
   * Commonly there is only one ``Publisher`` (for a given Topic); that is not mandatory, however.


.. method:: Topic.publish(value, force=False):

   This method is called by the ``Publisher``, whenever a new **value** is to be shared. When **force** is `False`
   (default), the ``value`` will only be distributed when it differs from the previous value. To force distribution, set
   **force** to `True`.

.. method:: Topic.subscribe(callback):

   This method is called by all ``Subscribers`` to *register* a **callback**, which is called on new ‘data’.

   .. _PubSub_callback_signature:

   The passed **callback** (any `callable`, like a :func:`~pubsub.AbstractType.callback_function_type`
   :meth:`~pubsub.AbstractType.callback_method_type`) will be called when ‘data’ is available. It
   has a signature like::

     def callback([self,] value, topic):

   Where **value** is the ‘data’ passed to :meth:`publish` and  ‘**topic**’ is the :class:`~pubsub.Topic`
   instance, use to route it.

   When the callback is a method, the `self` parameter is automagically remembered by Python. For function-callbacks,
   leave it out.

Supporting types
================

.. currentmodule:: pubsub.AbstractType

Both the ``Publisher`` and the ``Subscribers`` are *Abstract Types*.

.. class:: Publisher

   Any code that will call :meth:`pubsub.Topic.publish`. It can be a class, a module or just code ...

.. class:: Subscriber

   Everybody calling :meth:`pubsub.Topic.subscribe`. Typically, the :class:`Subscriber` has a **callback**
   function/method too. See :ref:`PubSub_callback_demo` for an example.

   Often, it has a method that acts as the callback.


callbacks
---------
The generic signature for callbacks is simple:

.. function:: callback_function_type(value, topic)
.. method:: callback_method_type(self, value, topic)

