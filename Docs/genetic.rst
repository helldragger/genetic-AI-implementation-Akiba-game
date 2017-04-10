A genetic algorithm
===================

* :ref:`Why using a genetic algorithm?<why>`
* :ref:`The genetic module<genetics>`

.. _why:

Why using a genetic algorithm and not a neural network?
-------------------------------------------------------

There are 3 parameters which determined what kind of algorithm I could use to make this AI:

    1. I wanted to make this whole system dependence-free

    Home made code source permitted me to maximise compatibility between machines, and I learnt quite a lot doing
    this alone with my own research, more, I also had to learn and understand how to use some kind of optimizations like
    the alpha beta pruning to reduce a minmax or negamax algorithm time consumption.

    2. I had no training data nor the possibility to determine by myself what is a better move than another.

    The lack of training data kept me from using a deep learning neural network and my incapacity to determine
    which move is really the best in any situation of this game kept me from using a positive reinforcement based learning
    neural network, having only some abstract and arbitrary rules and no way of fine tuning manually the best
    configuration myself, I naturally choose to use a genetic algorithm to fine tune it by itself!

    3. I never did that, and I f*****g love challenges to understand and resolve

    This factor is probably as important than the two above. I love learning new things and de-cypher new concepts
    from the headache to the wonderful moment where I finally understood the mechanics and successfully used it somewhere


I'm not going to lie, my code might seem a bit messy and unoptimized at some points but there is hopefully more to come.
I will not be satisfied of this program until it won't be properly multi-threaded, improved, and perhaps moar stats
using each generations data.

Let's dive in!

.. _genetics:

The genetic module
------------------

.. automodule:: bin.AI.genetics
    :members:


The genetic database
--------------------

.. automodule:: bin.database.genobase
    :members:
