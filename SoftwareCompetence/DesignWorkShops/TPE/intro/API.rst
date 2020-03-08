.. Copyright (C) 2017-2019: ALbert Mietus.

.. _TPE_API:

The TPE API
===========

Conceptually, a TPE is very easy to use. There are two main classes; the :class:`TPE` itself, and some :class:`FutureObject`\s.


.. class:: TPE

   Abstraheert een *WorkersPool*, inclusief queues, etc.
   |BR|
   *Gemoduleerd naar de Python implementatie ``ThreadPoolExecutor``; maar veel eenvoudiger.*

   Het (maximaal) aantal worker moet bij het instantiëren van de class opgegeven worden.

   .. method:: submit(fn, *args, **kwargs)

   Voor een nieuwe taak op en return een :class:`FutureObject`.  De functie ``fn`` zal asynchroon
   uitgevoerd zal worden als ``fn(*args, **kwargs)``.

.. class:: FutureObject

   *Gemoduleerd naar de Python implementatie ``Future``; maar veel eenvoudiger.*

   .. method:: done()

      Return ``True`` als de taak afgerond is; anders ``False``. Wacht nooit op een taak.

   .. method:: result(timeout=0)

      Return het resultaat van de bijbehorende taak, als dat al beschikbaar is. Als die taak nog
      niet afgerond is, dat zal daar maximaal *timeout* seconden op gewacht worden. Als de taak dan
      nog niet afgerond is, zal ``None`` terug geven worden

