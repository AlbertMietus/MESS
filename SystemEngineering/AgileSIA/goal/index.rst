.. Copyright (C) ALbert Mietus; 2023, 2024

**********
Objectives
**********

The goal of an SIA is to *analyse* the impact of a feature (or change) and *apprise the PO* of the options he has to
achieve it.  It typically results in a document --but the document is *not* the goal (and shouldn't be)!

As we will see below, the goal of the SIA is to guide the next development steps: Does it bring (business) value?
*(typically: yes)* and what is the best option to realise it? After making those two decisions, the impact analysis
--and the SIA document itself-- quickly loses its value.
|BR|
In that view, the write-a-document part can even be considered a waste! That is not what I recommend, however. A written
document is also helpful for discussing and reviewing the SIA.


Business value
==============

Before one can decide whether and how a feature brings value, one needs insight into the necessary investment [#estimate]_
This is not only (development) *costs* (sw: mostly man-hours). Usually, *duration* (Time-2-Realize, or
Time-2-Marked) and *risks* (e.g. to introduce bugs) are as important. Depending on the ecosystem, other topics should be
addressed too.

Generally, there are multiple (technical) means to accomplish the same innovation [#ISW]_, [#OneShot]_. The SIA should
offer a few (typically: 3 main) solutions, possibly with variants. They all fulfil the demands but differ in
quality, luxury, and more relevant for the PO: primary value and investments.

Common mistakes
===============

* A SIA can get too technical and appear more like a design document, which makes it difficult for people to understand
  the impact. And to expenses to write.

  As a consequence, deciding not to go forward becomes impractical.
  |BR|
  At the same time, it’s often “too much work” to offer multiple solutions. Then, there is nothing to choose. --making
  the SIA useless.

  * A design (phase & document) may be needed --even in a lean, agile approach. It is planned after the SIA.
  * Remember, should the PO lower the priority --based on the Agile SIA-- the design effort has become a waste.
  * Even when not: When the SIA present three options and so three designs are made, we use only one.

* Not thinking about **design options**.
  |BR|
  Sometimes only one option is presented. Then, the PO can’t choose. But usually, it implies somebody else has made the
  choice (implicitly). That is not the role of the team.

* No upfront **design thinking**. This is the other extreme of the first mistake (too much design), and as bad.
  |BR|
  Even though the document shouldn't be “too technical” (*as it should focus on business value, and in the language of the PO*), that
  does not imply the team has to think about the design. A bit of “whiteboard design” is needed, to estimate the cost
  (etc) of that option.

  * There is no need to convert those (3) design sketches into real designs and present them in the SIA.
  * Only the effect of that design is presented to the PO (and so globally described in the SIA)

  .. note:: Remember those sketches

     It is wise to store all those sketches, and possibly some notes, for later. Most likely one of the three will be
     needed in an upcoming phase/sprint. Then it (only one) will be converted into a real design and worked out.
     |BR|
     In a typical lean, agile approach, those provisional designs are stored as a photo in a wiki, along with the
     notes.

A SIA has 5 chapters
====================

As we present in :ref:`AgileSIA-5chapters`, an (agile, lean) SIA has five chapters, only 5!
|BR|
However, it not the exact number that counts -- some prefer to combine the 3 “solutions chapters” is a single chapters,
other may varie a bit on number of solutions, or the place of sub-chapters.

Still, using that template (as used in :ref:`SIA-demo`) will typically result in a nice SIA.



-----

.. rubric:: Footnotes & Links

.. [#estimate] In that (limited) view, an SIA is like a complicated planning session.
   |BR|
   Depending on (e.g.) costs, the PO may place the feature high, or low, on the prioritised backlog.

.. [#ISW] “*It Should Work*” is a common baseline. All presented options should work, as nobody will ever select one
   that doesn't. But it doesn't need to be perfect (see below).

.. [#OneShot] Mostly, software should be maintainable. *“Clean Code”* has business value in the long run.
   |BR|
   However, once and a while we need “One Shot” [#OneShot2]_ code, where this is less needed. Then, the PO may decide to
   go for a (cheaper) option that has less quality.

.. [#OneShot2] As an example: migration “scripts” to update data from version `x.1(a)` to `x.1(b)`  will never be used
   again after the update. Or a “Proof of Concept”; typically that code is written fast, to demonstrate the ability, then
   replaced by “real code” and thrown away.
   |BR|
   That kind of software is often written in “another language”. The risk that nobody can maintain it is absent.

