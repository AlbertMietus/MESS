.. Copyright (C) ALbert Mietus; 2023

.. _SIA-demo-H1:

=============================
1) The Bumper of a Muscle Car
=============================


.. seealso::
   This *first* chapter of the SIA is about requirements. Talk to **all** stakeholders, order and list **all** needs.
   The client (ProductOwner) should react with: “*Yes, this the bumper we need*”.

   -- :ref:`AgileSIA-5chapters`

.. Caution::

   * We mix the (shortened) text in this SIA with tips for the apprentice(s).
     |BR|
     Don’t do that in a genuine SIA.
   * We use an “interview style” for some needs to clarify the several demand types,
     |BR|
     You will not do that in most SIAs.

Assignment
===========

The client’s demand is simple:

.. demo:: Make a bumper
   :ID: BUMPER
   :tags: Bumper
   :project: AgileSIA

He reasons that whenever we are worth a penny,  we know how to deliver a bumper, know all the legal specs, etc.

Requirements
============

.. tip:: As you probably guessed, not “any bumper” will do. So, spend some time on *requirements gathering*.

.. req:: Build to impress
   :ID: BUMPER_chrome
   :links: BUMPER
   :tags: Bumper
   :project: AgileSIA

   As it is a Muscle Car, it should impress ordinary people. They generally like *bling-bling*, shiny stuff. So
   the car will have a lot of chrome. We mandate this for the bumper as well.

.. req:: We are in a hurry
   :ID: BUMPER_April1
   :links: BUMPER
   :tags: Bumper
   :project: AgileSIA

   We will race with this car on April 1! So, we need the bumper quickly. And we assume you know we need both bumpers
   mounted before we can start regulation. So, plz deliver it as early as possible!

.. tip:: Not all requirements are technical. Usually, there are also demands [#nf]_ on cost, duration, quality, etc. Above, you
         find an example.


.. req:: Front and Back
   :ID: BUMPER_1is2
   :links: BUMPER
   :tags: Bumper
   :project: AgileSIA

   Even though we always speak about “the bumper” --like everybody else-- every car needs two bumpers: one at the front
   and one at the back. And they are not the same!

   So, whenever we ask for one, plz deliver both! Although, I assume you already know that. ...

.. tip::

   This :need:`BUMPER_1is2` need is trivial. At least for some. But when your solution has it wrong is costly.
   |BR|
   Once in a while, a client will read a triviality and correct it. Then you saved even more.

   Remember: the goal of this chapter is simple: *Make sure you solve the right problem*.

.. req:: Impress me
   :ID: BUMPER_SafetyImago
   :links: BUMPER
   :tags: Bumper
   :project: AgileSIA

   We build a luxury, high-end car. Our clients like to be impressed. Surely we don’t want to spend a fortune on a
   bumper, but it shouldn't be cheap. Also, we prefer to give our clients a safe & secure car. So make sure that the
   bumpers are not only regulation-safe but also “visualise” that!

.. req:: Give me options
   :ID: BUMPER_Green
   :links: BUMPER
   :tags: Bumper
   :project: AgileSIA

   This is our first eco-friendly muscle car; we used to be “petrol heads”. -- therefore we call it *”Green”*.
   |BR|
   Saying that, as the chief project manager, it worries me too.  We have so many things to do, there are so many
   project risks, and we can’t afford to delay. Therefore, I’m very happy about your offer to help me with all those
   non-core items.

   What I’m basically saying is: “Give me options”. When you can deliver faster or find creative solutions, I am
   interested --even when it costs more. Then, I can give you more components and remove some risk from my planning.

.. tip::

   For this exercise, we stop here with the demands. You should now have a quite complete image of the bumper that is
   needed. And the (non-technical) demands for this mini-project.

   .. warning:: You can now continue with the next page, chapter: :ref:`SIA-demo-H2`.
      |BR|
      **OR,** you can think for a moment to find a few  creative solutions that fit all needs -- Give it a try!

-----

.. rubric:: footnotes

.. [#nf]
   Experienced architects will tell you that the non-technical *needs* are the most important ones. Typically, an
   architecture is driven by those “*non-functionals*”.
