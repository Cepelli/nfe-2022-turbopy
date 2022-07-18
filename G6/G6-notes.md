G6: turboPy Basics
==================

The need for a framework
------------------------

Equation and figure references refer to the [turboPy paper](https://doi.org/10.1016/j.cpc.2020.107607).

- Example physics problem [Eqs. 1-4]
- Numerical solution [Fig. 2]
- Possible workflow [Fig. 3] and implications for class design
- Note that details for given problem are mostly at "PhysicsModule" level

The framework of turboPy
------------------------

- "Core" vs "apps"
- Core of turboPy [Fig. 1]
- Example app [ChargedParticle and EMWave PhysicsModules](https://github.com/NRL-Plasma-Physics-Division/particle-in-field)

Live Example
------------
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/NRL-Plasma-Physics-Division/particle-in-field/HEAD?filepath=tutorial.ipynb)

- Clone turboPy
- Set up conda env for turboPy
- Clone example problem
- Run Example
- Plot outputs

What we will be doing
---------------------

- turboPy core: mostly documentation and testing
- turboPy apps:
    - particle-in-field: documentation and testing
    - beam-driven-breakdown (w/ASR): 1D model of how a pulsed electron beam can form a plasma in a low-pressure gas
    - Flux-Corrected-Transport (w/SBS): solve fluid equations with FCT algorithm
    - Advanced particle pusher (w/Dan Gordon): implement new algorithm
    - Particle-pusher test app (w/Dan G):
        - Volume preservation is discussed in some of the references.
        - Maybe we can think of some kind of app that is optimized to test the quality of volume preservation.  This hypothetical app would say “plug in your algorithm and I will tell you how well volumes in phase space are preserved.”
    - More ideas?
