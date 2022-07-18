# Testing Existing Code and Test Driven Development (TDD)

If you are brand new to testing I would recommend the getting started with testing on RealPython.\
[python-testing](https://realpython.com/python-testing/)


**Show of hands:** 
 - How many people here know what writing a test is?
 - How many of you have previously written a test?


**Example of a test with units:**

If and area is given in m<sup>2</sup> but we know we need to report the value in cm<sup>2</sup> we can do what is called an assertion 

```
area = 8  # [m^2]

assert area == 800
AssertionError: assert 8 == 800
```

"What is an assertion?"\
Assertions evaluate code with Boolean type logic to get some statement to pass or fail.

## Why is testing code a good idea?

Testing code verifys that your code is doing what it is designed to do and helps the developer/user find any bugs.

Tests can help improve the readablity of code for your future self and others. 


## What questions should you ask yourself?

Any questions are good question!!
 - Is this the right value?
 - Should this be dynamic or static?
 - Is this method doing what I want it to?
 - Does this compare to other data?


## Pytest

This tutorial is going to be based on pytest. Pytest is called a "test runner" which will collect all the tests and then execute them in what is your "testing suite". 

Examples of other runners are unittest, nose, tox, etc..

Many times tests can also become repetitive and you might find that tests are starting to look very similar. Code that may only differ from an input or an output might call for paramterizaiton or adding a test fixture.

Fixtures can house data that can be reused in different ways. A dictionary could need to be formatted in different way, thus you can create a fixture of that dictionary.  

**To use Pytest:**

```
>>> import pytest
>>> pytest test_file.py
```

More information on Pytest is located at 
[pytest](https://realpython.com/pytest-python-testing/)

## Test-Driven Development (TDD)

Is actually where you write the test first!

*The goal is actually to fail first!*

You have an idea for an application and actually the first thing you do is come up with a plan that will analyze each part of the application. You will end up breaking it down into testing the setup, any manipulation, and the expected respone from each maipulation that is preformed. 