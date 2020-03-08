.. Copyright (C) 2017-2019: ALbert Mietus.

Use (Examples)
==============

This entry gives a very simple example, in various languages.

The key methods are :meth:`TPE.submit()` and :meth:`FutureObject.result()` [``.get()`` in some languages]. Also
:meth:`FutureObject.done()` [or ``.isDone()] is a important method.
|BR|
There are many more methods, depending on the implementation. Bit without using the above ones, you not using it properly.

There are basically three steps:

1. Create the TPE object. This will start the workers (threads) and do the plumbing
2. Submit *callable*\s (functions) to the TPE. Which will distribute it to an available worker, or queue it temporally.
3. Use the result **later** by reading the returned :class:`FutureObject`.


When calling :meth:`TPE.submit()`, a :class:`FutureObject` is returned **directly**. This is kind of a placeholder; it
doesn’t contain the result yet! When the submitted function (eventually) returns, the return-value is stored in that
placeholder.

One call monitor the availability of the result by :meth:`FutureObject.done()`; only when it is ``True`` the result is
available. Or, one just wait for it by calling :meth:`FutureObject.result()`. Surely, then it is done.

Note: one can also give a wait-limit to :meth:`~FutureObject.result()`. See you language and/or implementation
documentation for details

Python
------

.. literalinclude:: examples/TPE_demo_1.py
   :language: python3

You can run this examples by (using python-3)

.. code-block:: shell-session

   [albert@MESS:1]% python examples/TPE_demo_1.py
   0: 5 ==> 25 (waited)
   1: 3 ==> 9 (direct)
   2: 6 ==> 36 (waited)
   #...

Java
----

.. literalinclude:: examples/TPE_demo_2.java
   :language: java

To compile this example, compile it first (int the examples dir)

.. code-block:: shell-session

   [albert@MESS:2]% javac TPE_demo.java
   [albert@MESS:3]% java TPE_demo_2 Task
   Future done (Y/N)? :true.	Result is: 1
   Future done (Y/N)? :false.	Result is: 49
   Future done (Y/N)? :false.	Result is: 64
   Future done (Y/N)? :true.	Result is: 9
   #...
