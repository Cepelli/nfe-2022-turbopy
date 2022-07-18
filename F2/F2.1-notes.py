# %% [markdown]
"""
 # What is Object-Oriented Programming (OOP)?

 OOP is a programming paradigm that you can use to model the real world (**or an imaginary one!**) in code.
  
 In OOP, we group related data and functions into "islands" of information known as **objects**.

 - object: packages both data and procedures that operate on that data
 - methods or operations: procedures within objects that act on the object's data or perform some other action
"""
  
# %% [markdown]
# Whether you realize it or not, you've already been doing OOP. It's inherent in Python.
#  
# For example, let's create a string:
i_am_a_string = "i am a string"

# %% [markdown]
# What kind of object is `i_am_a_string`?
print(f"object {id(i_am_a_string)} is of type {type(i_am_a_string)}")

# %% [markdown]
# Let's go look at the [documentation](https://docs.python.org/3/library/string.html) for `str` in Python.

# %% [markdown]
"""
 # Encapsulation
  
 An object performs an operation when it receives a **request** (or message) from a **client**.
  
 Requests are the *only way* to get an object to execute an operation.
  
 Operations are the *only way* to change an object's internal data.
  
 Therefore, an object's internal state is said to be 
 **encapsulated**--it cannot be accessed directly, and its representation 
 is invisible from outside the object.

 ***Note: encapsulation is not really enforced in python. 
 It's as if all attributes are "public", 
 in the c++ sense of "public"/"private" variables. However, some
 conventions have emerged such as starting variable and method names
 with underscores to indicate "private" attributes.***
"""

# %% [markdown]
# For example, for `str` objects, a `capitalize` method is defined:
i_am_a_string.capitalize()

# %% [markdown]
# But the actual value of `i_am_a_string` is unchanged.
print(f"object {id(i_am_a_string)} is still of type {type(i_am_a_string)} and value '{i_am_a_string}'")

# %% [markdown]
# But if we create a new string using the `str.capitalize` method:
i_am_a_capitalized_string = i_am_a_string.capitalize()
print(f"object {id(i_am_a_capitalized_string)} is of type {type(i_am_a_capitalized_string)} and value '{i_am_a_capitalized_string}'")

# %% [markdown]
# So, we see that the methods defined by the built-in Python `str` Class do not alter the string itself. This is because
# string objects in Python are immutable sequences of text.

# %% [markdown]
# Let's check out some objects in numpy.
import numpy as np
i_am_a_numpy_array = np.array([1.0, 2.0, 3.0])

# %% [markdown]
# But wait, I've done that long `print` statement several times. Perhaps we should define a function.
def print_object_info(object):
    print(f"object {id(object)} is of type {type(object)} and value '{object}'")

# %% [markdown]
# Now let's use our new function:
print_object_info(i_am_a_numpy_array)
print_object_info(i_am_a_numpy_array[0])

# %% [markdown]
# What type of object is `print_object_info`?
print_object_info(print_object_info)

# %% [markdown]
# How very meta!
#   
# Let's look at a method defined for numpy.array, [the `numpy.sum` method](https://numpy.org/doc/stable/reference/generated/numpy.sum.html).
i_am_a_numpy_array.sum()

# %% [markdown]
#
print_object_info(i_am_a_numpy_array)

# %% [markdown]
# Can we implement our own version of this method for Python lists?
#  
# Let's create a `BetterList` class that is a subclass of the `list` class.
class BetterList(list):
    pass

i_am_a_list = [1.0, 2.0, 3.0]

print_object_info(i_am_a_list)

i_am_a_better_list = BetterList(i_am_a_list)

print_object_info(i_am_a_better_list)


# %% [markdown]
# Our `BetterList` Class inherits all of the functionality of the `list` Class.
print(f"the first item is {i_am_a_better_list[0]}")
print(f"there is/are {i_am_a_better_list.count(1.0)} occurrence(s) of 1.0")
print(f"there is/are {i_am_a_better_list.count(4.0)} occurrence(s) of 4.0")

# %% [markdown]
# Does a `BetterList.sum` method exist?
i_am_a_better_list.sum()

# %% [markdown]
# Here is a re-definition of BetterList to include a `sum` method:
class BetterList(list):
    def sum(self):
        _sum = 0.0
        for item in self:
            _sum += item
        return _sum

# %% [markdown]
# Now does a `BetterList.sum` method exist?
i_am_a_better_list = BetterList(i_am_a_list)
print(f"sum of i_am_a_better_list: {i_am_a_better_list.sum()}")


# %% [markdown]
"""
What are some potential issues with BetterList.sum()?
"""

# %% [markdown]
"""
The method only really works for a list of floats, so we should
tell the user until all types of lists are implemented.
"""

class BetterList(list):
    def sum(self):
        if type(self[0]) is not float:
            raise NotImplementedError("sum implemented for lists of floats only")
        _sum = 0.0
        for item in self:
            _sum += item
        return _sum

# %% [markdown]
# # Object-Oriented Design (OOD)
#  
# The hard part: decomposing a system (or domain) into objects.
#  
# Why is it so hard? Many factors affect the decomposition, and often in conflicting ways:
#
# %% [markdown]
# ## encapsulation
# Favoring object composition over class inheritance helps to keep each class 
# encapsulated and focused on one task. Your classes and class hierarchies will 
# remain small an will be less likely to grow into unmanageable monsters. 

# %% [markdown]
# ## granularity
# Objects can vary tremendously in size and number. They can 
# represent everything down to the hardware or all the way up to entire 
# applications.

# %% [markdown]
# Other competing factors:
# - dependency
# - flexibility
# - performance
# - evolution
# - reusability
# - and on and on

# %% [markdown]
# Let's look at [turboPy core.py](https://github.com/NRL-Plasma-Physics-Division/turbopy/blob/main/turbopy/core.py)
# and discuss some of the basic OOP concepts at work.
# %%
