Introduction to Python
======================
*Time to complete: 30-50 hrs, depending on how much you experiment with code in L&L* 

*Seminar date: 10:00 A.M. Eastern, Wednesday, June 23, 2021*

Prep
----
1. Complete the RealPython [Intro to Python Learning Path](https://realpython.com/learning-paths/python3-introduction/).
2. Read [Managing Environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#) from the conda documentation. Pay particular attention to documenting, creating, and managing environments from an environment.yml file.
3. Read sections 1.2 through 1.8 (middle of page 5 through page 36 of the PDF) of [Linge and Langtangen (L&L)](https://link.springer.com/book/10.1007/978-3-030-16877-3). 
Try to copy most if not all of the code in the text into VS Code and experiment with it (either in a [Jupyter Notebook](https://code.visualstudio.com/docs/python/jupyter-support) or using
[Python Interactive](https://code.visualstudio.com/docs/python/jupyter-support) mode) by
changing some values for variables and seeing what happens. 
As the text says at the beginning of Section 1.2.5, *"[Programming] is very much like learning to swim. Nobody can do that
by just reading about it!"*

Seminar Goals
-------------
Discuss basic Python concepts, share solutions to homework problems, and discuss anything interesting you learned while experimenting with the code in the text. 

Homework
--------
1. Create a folder `F1-lastname` in the `F1` folder of this repo to contain your homework.
2. Create, activate, use, and update as required a conda environment for your homework. Use an environment.yml file to document, create, and manage the environment.
3. Complete any two of the six exercises in Section 1.9 of [L&L](https://link.springer.com/book/10.1007/978-3-030-16877-3)
4. (Optional) Add one or more bullets to the Notes section below.
5. (Optional) Add any code that you generated while experimenting with code in L&L that you would like to share.

Notes
-----
- Consider creating one or more "bootcamp" Jupyter Notebooks or `.py` files with comments and code blocks for keeping notes from all
  of your learning. You can use the markdown feature to add notes. This will also allow you to save commonly used commands.
- `conda` environments are a great way to manage a development environment, allowing you
  to know **exactly** which version of 
  a given package that you are using, and conda takes care of dependencies.
- Make sure to install and use pylint whenever you create a new python file. It makes sure that your python complies with certain standards of readability and neatness, and makes it easier for others to review and understand your code.
- When writing code, don't get too hung up on making it perfect the first time. Obviously there are rules and guidelines that you should
  always try to follow, but there are plenty of tools such as pylint that help you catch formatting errors and general ugliness. Use these tools
  frequently during and after development to revise your code and increase its readability and efficiency.