.. Copyright (C) ALbert Mietus & Sogeti.HT; 2020

***********************
Some notes on this demo
***********************
:status: Just notes


To be able to make a compact demo, some “tricks” are used; like the “forgotten test”. Those tricks are documented here.

.. _about_forgotten_test:
The forgotten_test
==================

Intentionally, for the first demo one test is “forgotten”. This shown and documented in :ref:`forgetting a test <forgotten_test>` on one page, but needed to be fixed for the second demo; see :ref:`test_hotfix` on another page. And test:need:`CALC2_TEST_DIV_1` itself.
and combining some

Surely this is not typical in one documentation-release. Therefore the ``:tags:`` `general`, `calc1` and `calc2` are used in the ``req::` and ``:spec`` *directives*, to be able to filer them in the tables and graphs.


LATER/ADD
=========

* We can count the numbers of test, and we can insert links to each one automatically. By example, for the calculator requirements:

  :need:`CALC_ADD`:  has :need_count:`type=='test' and 'CALC_ADD' in links` tests defined. (:need_incoming:`CALC_ADD`)

  The count is only selecting the TEST. The list is alos showing the SPEC!

* Count/Ref all or only 1 step?

  :need_count:`type=='test' and 'CALC1' in links` test for CALC1.

Demo Notes
===========
