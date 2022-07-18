Refactoring and the Factory Method Design Pattern
=================================================
*Time to complete: 20-40 hrs, depending on complexity of refactoring exercises chosen* 

*Seminar date: 10:00 A.M. Eastern, Friday, June 25, 2021*

Prep
----
1. Complete the RealPython tutorial [Refactoring Python Applications for Simplicity](https://realpython.com/python-refactoring/).
2. Read the RealPython post [The Most Diabolical Python Anti-Pattern](https://realpython.com/the-most-diabolical-python-antipattern/).
3. Read the RealPython article [The Factory Method Pattern and Its Implementation in Python](https://realpython.com/factory-method-python/).

Seminar Goals
-------------
Share any examples of code that you found in NRL open source projects that
would benefit from refactoring as well as any suggestions that you have or
actual refactoring that you completed. Also, share any good or bad examples of
code complexity that you discovered in your analysis. Discuss common sources
of code complexity and the issues that arise from it.
 
Homework
--------
1. Try to add at least one item to the Notes section below.
2. Use `wc`, `radon`, and `wily` to measure the complexity of a NRL Python open source project
and document your findings in a markdown file.  NRL open source projects written in Python can be found at [https://github.com/NRL-Plasma-Physics-Division?language=python](https://github.com/NRL-Plasma-Physics-Division?language=python) and [https://github.com/USNavalResearchLaboratory?language=python](https://github.com/USNavalResearchLaboratory?language=python). 
3. Search NRL Python open source projects and try to identify at least one complexity anti-pattern or other opportunity to improve code through refactoring. Document your findings in a markdown file. If you are able to fork the repo and do the refactoring, add a link to your forked code.

Files
-----
Use the `A1-lastname-` prefix for any files that you add. 
If necessary, create an `A1-lastname` subfolder to contain multiple files.

Notes
-----
- The flag `-a` can be used with `radon` to measure the average complexity of a directory. Using the `-s` flag prints out the details of the analysis.
- The Halstead metrics are Length (number of operators and operands), Vocabulary (number of *unique* operators and operands), Volume (product of length and vocabulary), Difficulty (half the *unique* operators multiplied by the rate of operand reuse) and Effort (product of volume and difficulty). They all estimate different aspects of a program's complexity.
- Not all metrics for measuring complexity have equal value or should be minimized at all costs — for example, trying to minimize lines of code (LOC) can lead to creating unreadable code at the expense of a lower line count.
