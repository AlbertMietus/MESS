.. _AgileSIA-5chapters:

The 5 chapter template
======================

It might help to use the following template to understand the goals of the SIA. And assist in writing a sound one.

An SIA usually consists of only five chapters:

1. The Problem Analyse
----------------------

This is a bit like a Requirements Gathering phase. Usually one has to communicate with all stakeholders (or read
their inputs) to thoroughly understand and list their needs.  All the requirements and desires should be listed in
natural language and presented in a logical manner [#NoInterview]_.
|BR|
There is no need to select or prioritise the demands at this stage.

In many cases, the stakeholders have already expressed their input and one uses mainly other (“higher”) documents
as input. Remember, however, it’s about what the stakeholders want, not about the documents themselves.
|BR|
Do not “copy” all those demands. Just mention them, link to the source and summarise them such that the document is
readable.

More often than not, this is a short chapter, maybe a few pages. The goal is that the PO and all stakeholders
say: “Yes, that is exactly what we need” [#check]_.

2.  Solution A
--------------

It gives a highlight of the first presented (design) option, without explaining the design. Just enough so that the
PO (and other stakeholders) understand it -- there is no need that anybody can implement it already.

Then, the cost, risk, duration and other relevant topics (for the stakeholders) are explained.
|BR|
Again, keep it simple and global. Don’t try to convince the PO; (s)he will (should) trust your analysis.

Optionally you can present some sub-options. But don’t go into details. Only sub-options that are relevant for the
PO are relevant.

3. Solution B
--------------

Same as above, but (completely) different.
|BR|
Sometimes a feature can be split into several functional “slices” [#cake]_.

Different solutions may come with different slices, but we can also have common ones. Then, introduce them early, and
refer to them in the next solution(s).  Make it explicit which slices are (partially) common and which not.
|BR|
Despite that slices can be common, they may have other effects on investments (costs etc), risk or other business
values Therefore, I prefer to write out those aspects in each solution. Often assisted with a phrase as *“a bit
more/better/... than in ..”*

4. Solution C
-------------
Again, another way for the same result [#cents]_.

5. Summary/Overview
-------------------

This short chapter lists the relevant differences (for the PO/stakeholders) between the solutions, often in a table.

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

.. [#NoInterview] Plz, don’t make it a conversation report. Don’t use stakeholder order. And always use your own words.
.. [#Check] Typically this 1st chapter is reviewed early. This chapter is also a check: When the team misunderstands the
   feature, it is better to fail fast.

.. [#cake] A cake is (typically) cooked bottom-up and consumed left-to-right. Even though the sum of the layers and the
   sum of the slices are equal, the effect differs. I often use this analogy and will write a blog about it
   “soon”. For now, plz just remember it does differ and get used to the term:-)

.. [#cents] Be “`Pound Wise and Penny Foolish <https://www.dictionary.com/browse/penny-wise-and-pound-foolish>`__”!
   |BR|
   Nobody is (or should be) interested in a solution that differs only in a few (pre)cents. Not in an (upfront) SIA
   document. Unless, of course, when that percentage is a relevant business topic.

