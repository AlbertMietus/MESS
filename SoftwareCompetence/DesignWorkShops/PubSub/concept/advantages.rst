.. Copyright (C) 2020: ALbert Mietus.

Advantages
==========

For software-engineers, Pub/Sub has many advantages. The most obvious one is *decoupling*, another one is *scaling*. It
is also simple to :ref:`PubSub_use`.

And, with Pub/Sub you will automatically use
`‘Dependency Inversion’ <https://en.wikipedia.org/wiki/Dependency_inversion_principle>`_, one of the
`SOLID <https://en.wikipedia.org/wiki/SOLID>`_ principles; as well as
`‘Dependency Injection’ <https://en.wikipedia.org/wiki/Dependency_injection>`_, which often simplifies testing.


Coupling
--------

By and large, software-routines have to pass information. From one function to another, from one class to another, or
from one module to some other module(s). Especially this latter case is annoying when it is implemented by calling a
method of that other module. Then, we speak about **tight** (and *static*) **coupling**: the module effectively can’t
perform without the other. When that “other” module is a stable, generic *library*, it is often considered as
acceptable. Although it can disturb your (unit)-testing; by making it slow.

But how about two modules, that are under construction?
|BR|
Then, both are not “stable” (as they might develop) and being dependent on unstable modules is bad. You can’t test
independently, you may need to revise when the other is updated, etc. Well, you know the troubles ...

To overcome this, the modules should be *uncoupled* or *loosely coupled*: Both modules are not allowed to call a
function/method of the other one. (Which is easy:-). But still, pass information; which might seem impossible at first.

This is possible, as the modules do not depend on each other; instead, they both depend on the generic
:class:`pubsub.Topic`, as we can see on the :ref:`next page<PubSub_use>`


Scaling
-------

Now and then the same data is needed by multiple “consumers”. That number of “users” may even grow in future releases. A
sensor-value, by example, that was initially only used in one or two routines, may becomes relevant input to many new,
fancy features.

Imagine a module that handles (pushing) the brake. Initially, it was only needed to slow down the car. Nowadays it will
switch off the cruise control, also. Perhaps, in the future, that same data might influence the volume of the radio; or is
needed to automatically “e-call” 112, when there is a serious road accident. Or ...

With Pub/Sub, it is easy to distribute  data to more and more modules. Even to modules that aren’t yet imagined when you
write that sensor-routine! Your current module only has to use :meth:`pubsub.Topic.publish`, and that future module can
get that data using :meth:`pubsub.Topic.subscribe`; easy!

Questionnaire
-------------

We have shortly introduced two advantages, now you have to *think*

#. Are there **disadvantages** to this *design-pattern*?
#. Can you mention some other **advantages**?
