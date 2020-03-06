.. Copyright (C) 2017-2019: ALbert Mietus.

Use (Examples)
==============

This entry gives a very simple example, in various languages.


Python
------

.. literalinclude:: examples/sort_async.py

You can run this examples by (using python-3)

.. code-block:: shell-session

   [albert@MESS:1]% python examples/sort_async.py
   0: 5 ==> 25 (waited)
   1: 3 ==> 9 (direct)
   2: 6 ==> 36 (waited)
   #...

Java
----

.. literalinclude:: examples/SortAsync.java

To compile this example, compile it first (int the examples dir)

.. code-block:: shell-session

   [albert@MESS:2]% javac SortAsync.java
   [albert@MESS:3]% java SortAsync Task
   Created : Task 1
   Created : Task 2
   Created : Task 3
   #...
   Created : Task 9
   Created : Task 10
   Executing : Task 1
   Executing : Task 4
   Executing : Task 2
   #...
