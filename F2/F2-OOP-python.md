Object-Oriented Programming (OOP) With Python
=============================================
*Time to complete: 60-120 hrs, depending on complexity of chosen exercises from L&L*

*Seminar dates:*
- *F2.1: 10:00 A.M. Eastern, Wednesday, June 30, 2021*
- *F2.2: 10:00 A.M. Eastern, Wednesday, July 7, 2021*
- *F2.3: 10:00 A.M. Eastern, Wednesday, July 14, 2021*

Prep
----
1. Complete the RealPython [OOP with Python Learning Path](https://realpython.com/learning-paths/object-oriented-programming-oop-python/)
2. Read chapters 2 through 6 (sections 6.5-6.7 are optional) of [Linge and Langtangen (L&L)](https://link.springer.com/book/10.1007/978-3-030-16877-3). 
Just like with chapter 1, try to copy most if not all of the code in the text into VS Code and experiment with it (either in a [Jupyter Notebook](https://code.visualstudio.com/docs/python/jupyter-support) or using
[Python Interactive](https://code.visualstudio.com/docs/python/jupyter-support) mode) by
changing some values for variables and seeing what happens. 

Seminar Goals
-------------
- Review Object-Oriented Programming (OOP) with Python and how it is used in turboPy, nepc, and other NRL projects. Review concepts from L&L chapters 2 through 6.
- F2.1: Discuss the first third of the RealPython OOP Learning Path (through ["Supercharge your classes with Python super()"](https://realpython.com/courses/python-super/). Discuss L&L chapters 2 and 3.
- F2.2: Discuss the middle third of the RealPython OOP Learning Path (["Inheritance and Composition: A Python OOP Guide"](https://realpython.com/courses/inheritance-composition-python/) and ["OOP Method Types in Python"](https://realpython.com/courses/python-method-types/)). Discuss L&L chapters 4 and 5.
- F2.3: Discuss the remainder of the RealPython Learning Path and share an example of an OOP approach in your exercise solution. Discuss L&L chapter 6 (sections 6.5-6.7 are optional).

Homework
--------
1. Add a note to this markdown file describing at least one OOP concept used in turboPy, nepc, or another NRL open source project of interest.
2. Choose one of the exercises from the end of each assigned chapter of [L&L](https://link.springer.com/book/10.1007/978-3-030-16877-3), and submit your solutions in a sub-folder of `F2` named `F2-lastname`. You should have five code submissions (one for L&L section 2.5, one for L&L section 3.4, etc). Use at least one OOP approach in each of your solutions. In section 6.8, choose from the first four exercises if you did not complete the optional sections 6.5-6.7.

Notes
-----
* The "PhysicsModule" class uses inheritance to have the same basic attributes as its parent class: "DynamicFactory"
* Classes such as Simulation, Grid, and Diagnostic can be used inside the framework where we can use their attributes and methods for common issues.
* The Simulation class uses composition: it is composed of PhysicsModules, Diagnostics, ComputeTools, a clock, and a grid, all of which can function within the framework of the simulation.
* Several classes within computetools.py use super() to use parent class methods without activating the parent class