# %% [markdown]
# # Introduction to Python Notes

# Let's highlight some code in NRL open source projects that implement some key concepts from the 
# RealPython [Intro to Python Learning Path](https://realpython.com/learning-paths/python3-introduction/).

# ## String Formatting and f-Strings

# In [SIMDIS Software Development Kit (SDK)](https://github.com/USNavalResearchLaboratory/simdissdk/blob/9eaee25b2090b6cd1aee4a08818444fcf0ebc341/Examples/VelocityLayerTest/DownloadNws.py#L51-L52),
# we need today's date in YYYYMMDD format.

# %%
from datetime import datetime

today = datetime.today()
DATE = f"{today.year}{str(today.month).zfill(2)}{str(today.day).zfill(2)}"

print(DATE) 

# %% [markdown]
# `today.year`, `today.month`, and `today.day` are of type `int`.
type(today.month)

# %% [markdown]
# f-strings will use the ("dunder" or "special" or "magic" method) `__str()__` 
# defined for `int` objects to automatically
# do the conversion to a `str` type so...
year_string_1 = str(today.year)

# %% [markdown]
# ...is equivalent to...
year_string_2 = f"{today.year}"

year_string_1 == year_string_2

# %% [markdown]
# What if we just concatenate the year, month and day without `zfill`'s?  
# 
# (This works fine 65 days out of the year.)  
print(f"{today.year}{today.month}{today.day}")

# %% [markdown]
# `zfill` is a method defined for type `str`
help(str.zfill)

# %%
str(today.month).zfill(4)

# %%
print(f"{today.year}{str(today.month).zfill(2)}{str(today.day).zfill(2)}")

# %% [markdown]
# We can actually avoid the use of `zfill` all together 
# with built-in string formatting:

print(f"{today.year}{today.month:02}{today.day:02}")

# %% [markdown]
# ## Measure execution time with `timeit`
#
# If something like the above were used a lot in our code (like
# in a `for` loop), we might want to investigate which approach 
# runs the fastest.
import timeit
num_loops = 1000000

# %%
timeit.timeit('DATE = f"{today.year}{today.month:02}{today.day:02}"', 
              number = num_loops, 
              globals=globals())

# %%
timeit.timeit('DATE = f"{today.year}{str(today.month).zfill(2)}{str(today.day).zfill(2)}"', 
              number = num_loops, 
              globals=globals())

# %%
timeit.timeit('DATE = f"{str(today.year)}{str(today.month).zfill(2)}{str(today.day).zfill(2)}"', 
              number = num_loops, 
              globals=globals())

# %% [markdown]

# ## Use of `dict` in nepc

# In [nepc](https://github.com/USNavalResearchLaboratory/nepc),
# we have a [script for building a database of electron scattering cross-sections](https://github.com/USNavalResearchLaboratory/nepc/blob/90631a3ce7d3c43c7cd132e3bb5bcdeeef727568/nepc/mysql/build.py). 
# The [CS_DTYPE](https://github.com/USNavalResearchLaboratory/nepc/blob/90631a3ce7d3c43c7cd132e3bb5bcdeeef727568/nepc/mysql/build.py#L436-L455)
# dictionary stores the Python data types for each of the columns in the `CS`
# table of a nepc database.
#    
# `CS_DTYPE` is passed to the [pandas `read_csv` method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) when [reading metadata from
# disk](https://github.com/USNavalResearchLaboratory/nepc/blob/90631a3ce7d3c43c7cd132e3bb5bcdeeef727568/nepc/mysql/build.py#L528-L531),
# streamlining the interface between data on disk to Python to the MySQL methods for
# [writing to the database](https://github.com/USNavalResearchLaboratory/nepc/blob/90631a3ce7d3c43c7cd132e3bb5bcdeeef727568/nepc/mysql/build.py#L537-L565).

# %% [markdown]
# ## Some homework examples
#
# Now let's look at some homework submissions and discuss the basic Python concepts
# that were used.
