.. Copyright (C) 2017-2019: ALbert Mietus.

.. _TPE:

ThreadPoolExecutor
==================

.. sidebar:: English & Dutch

   This workshop is mostly in Dutch and partly in English; as it is based on an existing Dutch documentation. Only the new
   parts are in English. Hopefully, more and more part will be translated.

   Deze workshop is gebaseerd op bestaande, Nederlandse teksten. Voorlopig zijn allen de nieuwe delen in het Engels.


.. post:: 2020/03/06
   :tags: DesignWorkShops
   :category:
   :location: Eindhoven
   :language: en nl


   This workshop is about the *ThreadPoolExecutor* (‘TPE’ for friends): a pool of workers implemented with
   Threads. This is a modern, advanced **design-pattern** available in many languages.

   You will get an introduction to the concepts, to be able to use the ‘TPE’. Also, we study Python implementation, to
   practice **design-analyse**.

The example code is both available in Python and Java; more languages will follow. As the python-TPE is open-source and
easy to read, that one is used for the design-analyse. In that exercise, you will analyse code to create some
design-diagrams afterward.

Last, you may use this concept in a next DesignWorkShop ...


As usual, this workshop has some sections named *Questionnaire*; those questions are meant to sharpen the mind. Thinking
about the answer is more important that the answer itself.
|BR|
Some exercises will have a possible elaboration; often that isn’t only good one. Again: think about it. And learn!


---Have fun, Albert


.. toctree::
   :glob:
   :maxdepth: 2

   intro/index

   */index


------------------------

.. seealso::

   ThreadPoolExecutor (python)
      De referentie voor deze opdracht.
      https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor

   Future-Objects (python)
      Meer over (python) future-objects is te vinden op:
      https://docs.python.org/3/library/concurrent.futures.html#future-objects

   ProcessPoolExecutor (python)
      De proces variant heeft (vrijwel) dezelfde interface (en gezamelijke code). Voor liefhebbers is de
      documentatie te vinden op:
      https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor

   Java
      * Ook Java heeft een ThreadPoolExecutor; zie:
        https://docs.oracle.com/javase/7/docs/api/java/util/concurrent/ThreadPoolExecutor.html
      * En kent kent het Future-object, (o.a.) als interface. Zie:
        https://docs.oracle.com/javase/7/docs/api/java/util/concurrent/Future.html

   C#
      * In C# bestaan wel Thread-Pools:
        https://docs.microsoft.com/en-gb/dotnet/articles/csharp/programming-guide/concepts/threading/thread-pooling
      * Maar lijken Future-object niet te bestaan. Zie in bovenstaande de opmerkingen over `.. and
        return values <https://docs.microsoft.com/en-gb/dotnet/articles/csharp/programming-guide/concepts/threading/thread-pooling#thread-pool-parameters-and-return-values>`__

   C++
      * Er lijkt weinig ondersteuning in C++ voor worker-pools en futures.
      * *Boost* (http://www.boost.org) levert wel een aantal oplossingen (als library-code). Onderstaande
        links verwijzen naar de documentatie daarvan.

        - `basic_thread_pool <http://www.boost.org/doc/libs/1_63_0/doc/html/thread/synchronization.html#thread.synchronization.executors.ref.basic_thread_pool>`__
        - `futures <http://www.boost.org/doc/libs/1_63_0/doc/html/thread/synchronization.html#thread.synchronization.futures>`__

   `Blocks in C`
       Met deze C-extensie zijn functie inlines te definiëren. Het zijn een soort van
       *lambda*\-expressies, die gebruikt worden als argument in :c:func:`GCD.dispatch` functies.
       O.a de `CLang <https://en.wikipedia.org/wiki/Clang>`__ ondersteund dit.

       Zie https://en.wikipedia.org/wiki/Blocks_(C_language_extension)

       .. hint:: This extension does need a *runtime* (library) too.
