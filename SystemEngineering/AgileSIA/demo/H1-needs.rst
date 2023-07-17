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
   * To clarify the several kinds of demands, we use a bit of “interview style” wording in some needs.
     |BR|
     You will not do that in most SIAs.

Assignment
===========

The client’s demand is simple:

.. demo:: Make a bumper
   :ID: BUMPER
   :tags: Bumper
   :project: AgileSIA

   He reason, that whenever we are worth a penny,  we know how to deliver a bumper, know all the legal specs, etc.

Requirements
============

.. tip:: As you probably guessed, not “any bumper” will do. So spend some time on *requirements gathering*.

.. req:: Build to impress
   :ID: BUMPER_chrome
   :links: BUMPER
   :tags: Bumper
   :project: AgileSIA

   As it is a Muscle Car, it should impress common ordinary people. They generally like *bling-bling*, shiny stuff. So
   the car will have a lot of chrome. It is needed this also required for the bumper.


.. req:: We are in a hurry
   :ID: BUMPER_April1
   :links: BUMPER
   :tags: Bumper
   :project: AgileSIA

   We will race with this car on April 1! So, we need the bumper quickly. And we assume you know we need both bumpers
   mounted on the car before we can start regulation. So, plz deliver it as early as possible!

.. tip:: Not all requirements are technical. Usually, there are demands on cost, duration, quality etc too. This is just
         an example.


.. req:: Front and Back
   :ID: BUMPER_1is2
   :links: BUMPER
   :tags: Bumper
   :project: AgileSIA

   Even we --like everybody else-- always speak about “the bumper”, every car needs two bumpers: one at the front and one
   at the back. And they are not the same!

   So, whenever we ask for one, plz deliver both! Although, I assume you already know that. ...

.. tip::

   This :need:`BUMPER_1is2` need is trivial. At least for some. But when your solution has it wrong is costly.
   |BR|
   Once in a while, your client will read it, and correct it. Then you saved even more

   Remember: the goal of this chapter is simple: *Make sure you solve the right problem*.

.. req:: Impress me
   :ID: BUMPER_SafetyImago
   :links: BUMPER
   :tags: Bumper
   :project: AgileSIA

   This is a luxury, high-end car. Our clients like to be impressed. Surely, we don’t want to spend a fortune on a
   bumper, but it shouldn't be cheap. Also, we prefer to give our clients a safe & secure car. So make sure that the
   bumpers are not only regulation-safe but also “visualise” that!

.. req:: Give me options
   :ID: BUMPER_Green
   :links: BUMPER
   :tags: Bumper
   :project: AgileSIA

   This green muscle car is new for to, we used to be “petrol heads”. We are learning fast to build the first
   environmentally friendly Muscle Car -- therefore we call it *”Green”*.
   |BR|
   Saying that for me as the chief project manager, it worries me too.  We have so many things to do, there are so many
   project-risk, and we can’t afford to delay. Therefore, I’m also very glad about your offer to help me with all those
   non-core items.

   What I’m basically saying is: “Give me options”. When you can deliver faster, or find a creative solution --even
   when it costs more -- I would be interested.  Then I can give you more components, and remove some risk from my
   planning.

.. tip::

   For this exercise, we stop here with the demands. You should now have a quite complete image of the bumper that is
   needed. And the (non-technical) demands for this mini-project.

   .. warning:: You can now continue with the next page, chapter: :ref:`SIA-demo-H2`.
      |BR|
      **OR,** you can think for a moment, to find a few  creative solutions that fit all of the above needs -- Give it a try!
