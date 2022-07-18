# Refactoring and the Factory Method Design Pattern

## What is “refactoring” code?

When you are programming, there are multiple **different ways** to write code that has the **same result**:

```python
x = 5
y = 3
z = x + y
```

If you change code so that it achieves the same result but in a different way, that is called _refactoring the code_

```python
initial_height = 5
added_height = 3
total_height = initial_height + added_height
```

Do you notice anything different about the two examples above? What are some reasons one version of the code might be preferred vs another?

## Why would you rewrite code?

- If refactoring doesn't change calculation results, or the behavior of the code, why change it?  
    _Because sometimes, we do need to change the behavior of the code_

- Certain ways of writing code makes it easier to update or extend
- Remember: you are writing code to tell the computer what to do, but also for other people!
- These other people (including your future self) will appreciate having code that is clear and easy to read and modify

## Some thoughts on the factory design pattern

- _What is an "interface"?_  
In this context, an interface is the set of variables or methods that a class has. If two classes both have the same methods, then a programmer can use them interchangeably
- _Why use an interface instead of just using a bunch of objects that do what you need to get the job done?_  
Coding to an interface can give you code that is more reusable, more testable, better separated from other code, more extendible, etc.

## How is the factory design pattern used in turboPy?

- From RealPython: Factory Method is a creational design pattern used to create **concrete implementations** of a **common interface**
- In turboPy, the interfaces are defined by abstract base classes: hint, search for `raise NotImplementedError`
- Creating new “apps” in turboPy involves defining new `PhysicsModules` and `Diagnostics`
- These new classes are **concrete implementations** of the base `PhysicsModule` or `Diagnostic` classes
- The Simulation class then uses the factory design pattern to create instances of these new classes
- In this way, the Simulation class can be extended without having to modify any code in the core turboPy framework

## Example: PhysicsModule which defines a function on the grid

https://github.com/arichar6/refactoring_example

- Use a `PhysicsModule` subclass to define a function on the grid, and its derivative
- Pass parameters to `__init__` in a dictionary
- Define two functions, `set_profile` and `set_ddr_profile` which parse the parameters and set the function and its derivative
- It is easy to introduce a bug because of the “switch” that looks for the profile shape
- Note that the “switch” statement is repeated twice, and that it also mixes the “what” with the “how”

## Refactoring the example

- There are some “code smells” here that we should try to get rid of
- One is the redundancy in the code with the repeated logic for picking between functions 
- Another is the tight coupling in the code, between what it is trying to do (choose a functional form) and how it is doing it (with lambda functions mixed into the dictionary)
- We will try and get rid of these, and will find that in doing so, we naturally create a **common interface** that we can code to. 
- This sort of problem has been solved before… it’s exactly what the factory pattern is designed to solve

## To learn more
Recommended textbook: [99 Bottles of OOP](https://sandimetz.com/99bottles)


