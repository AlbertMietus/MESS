.. Copyright (C) ALbert Mietus; 2023

**********
Objectives
**********

The goal of an SIA is to *analyse* the impact of a feature (or change) and *apprise the PO* of the options he has to
achieve it.  It typically results in a document --but the document is *not* the goal (and shouldn't be)!

As we will see below, the goal of the SIA is to guide the next development steps: Does it bring (business) value?
*(typically: yes)* and what is the best option to realize it? After those two decisions are made, the impact analysis
--and the SIA document itself-- quickly loses value.
|BR|
From that view, the write-a-document part can even be considered a waste! That is not what I recommend, however. A
written document is also good to discuss and review the SIA.

Business value
==============

Before one can decide whether and how a feature brings value, one needs insight into the necessary investment [#estimate]_
This is not only (development) *costs* (sw: mostly man-hours). Usually, *duration* (Time-2-Realize, or
Time-2-Marked) and *risks* (e.g. to introduce bugs) are as important. Depending on the ecosystem, other topics should be
addressed too.

Generally, there are multiple (technical) means to accomplice the same innovation [#ISW]_, [#OneShot]_. The SIA should
offer a few (typically: 3 main) solutions, possibly with variants. They all fulfil the demands but differ in
quality, luxury, and more relevant for the PO: primary value and investments.

Common mistakes
===============

* Sometimes the SIA becomes more like a **design document**, with too many detailed technicalities.
  |BR|
  As a consequence, the  SIA phase is expensive, and deciding  not to go forward becomes impractical.  At the same time,
  it’s often “too much  work” to suggest more as one  solution; another limitation of the goal: select  the one with the
  most value.

  * Even in a lean, agile approach, the design (phase/document) may  still be needed. But it is planned *after* the SIA.
  * Remember, should the PO lower the priority --based on the Agile SIA--, the design effort has become waste.
  * Even when not: When the SIA present three option and so three design are made, we use only one.

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

.. _AgileSIA-5chapters:

The 5 chapter template
======================

It might help to use the following template to understand the goals of the SIA. And assist to write a sound one.

An SIA has typically (only) 5 chapters

1. The Problem Analyse.

   This is the Requirements Gathering part. One has to speak to all stakeholders to understand the needs and list them
   all. There is no need to select or prioritise demands and wishes. Just list them in natural language, and present them
   logically [#NoInterview]_.
   |BR|
   In many cases, the “stakeholders” have already expressed their input and one uses mainly other (“higher”) documents
   as input. Remember, however, it’s about what the stakeholders want, not about the documents themselves.

   More often than not, this is a short chapter, maybe a few pages. The goal is that the PO and all stakeholders
   say: “Yes, that is exactly what we need” [#check]_.

2.  Solution A

    It gives a highlight of the first presented (design) option, without explaining the design. Just enough so that the
    PO (and other stakeholders) understand it -- there is no need that anybody can implement it already.

    Then, the cost, risk, duration and other relevant topics (for the stakeholders) are explained.
    |BR|
    Again, keep it simple and global. Don’t try to convince the PO; (s)he will (should) trust your analyse.

    Optionally you can present some sub-options. But don’t go into details. Only sub-options that are relevant for the
    PO are relevant.

3. Solution B.

   Same as above, but (completely) different.
   |BR|
   Sometimes a feature can be split into several functional “slices” [#cake]_.

   Different solutions may come with different slices, but we can also have common ones. Then, introduce them once, and
   refer to the in the next solution(s).  Make it explicit which slices are (partially) common and which not.
   |BR|
   Despite that slices can be common, they may have other effects on investments (costs etc), risk or other business
   values Therefore, I prefer to write out those aspects in each solution. Often assisted with a phrase as *“a bit
   more/better/... than in ..”*

4. Solution C

   Again, another way for the same result [#cents]_.

5. Summary/Overview

   This short chapter list the relevant differences (for the PO/stakeholders) between the solutions, often in a table.

   It frequently also advice on **how** to select the best option. This is to guide the PO.
   |BR|
   By example:

   * *“Solution A has the shortest T2M, although it is twice as expensive”*.
   * *“When future extensibility is key, solution B offers the most flexibility”*.
   * *“Solution C has the main benefit that it has many slices, each can be realised independently in a series of
     sprints”*.
   * *“For the same reason, solution C can be implemented in 10 concurrent teams, keeping them fully loaded*
     |BR|
     (especially as we have the risk that two teams run out of work).”



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
   That kind of software is often written in “another language”. The risk that nobody is available to can maintain it
   is absent.

.. [#NoInterview] Plz, don’t make it a conversation report. Don’t use stakeholder order. And always use your own words.
.. [#Check] Typically this 1st chapter is reviewed early. This chapter is also a check: When the team misunderstands the
   feature, it is better to fail fast.

.. [#cake] A cake is (typically) cooked bottom-up and consumed left-to-right. Even though the sum of the layers and the
   sum of the slices add-op to the same, the effect differs. I often use this analogy and will write a blog about it
   “soon”. For now, plz just remember it does differ and get used to the term:-)

.. [#cents] Be “`Pound Wise and Penny Foolish <https://www.dictionary.com/browse/penny-wise-and-pound-foolish>`__”!
   |BR|
   Nobody is (or should be) interested in a solution that differs only in a few (pre)cents. Not in an (upfront) SIA
   document. Unless, of cause, when that percentage is a relevant business topic.

