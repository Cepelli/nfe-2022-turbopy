# %% [markdown]
"""
# A2 Seminar Notes

Let's look at the [NRL Evaluated Plasma Chemistry (nepc) 
package](https://github.com/USNavalResearchLaboratory/nepc)
and how it uses [pandas](https://pandas.pydata.org/) and 
[matplotlib](https://matplotlib.org/) under the hood.
"""

# %% [markdown]
"""
## Cross Section ($\sigma$)

***Cross section:*** a measure of the probability that a specific process 
will take place when some kind of radiant excitation (e.g. a 
particle beam or an X-ray) intersects a localized phenomenon 
(e.g. a particle). 

For example, an electron-impact excitation cross section for 
N$_2$ is a measure of the probability
that an electron of a given energy in a beam aimed at a nitrogen molecule will 
cause a specific excitation.

Cross sections are typically denoted with the symbol $\sigma$ 
(sigma), have units of area, and are a function of the energy and
type of the radiant excitation. 

In a way, the cross section in our above example can be thought 
of as the size of the nitrogen molecule as it appears to the electron. 
"""

# %% [markdown]
"""
## Electron Collision (Scattering) Processes in Plasmas

![](img/processes.png)
*From Meichsner, et al, "Nonthermal Plasma Chemistry and Physics," CRC Press, 
2013.*
"""

# %% [markdown]
"""
## Finding cross sections

Let's see a demo of accessing cross section 
data from [LXCat](https://nl.lxcat.net/data/set_type.php).
"""

# %% [markdown]
"""
## Exploring electron scattering cross sections with nepc

First, we import nepc and establish a connection to a 
MySQL nepc-formatted database of cross sections and
create a "cursor" for sending queries to the database.

*To actually develop in nepc may involve MySQL, 
which is beyond the scope of this seminar. But, just
in case someone can't resist, [here's the link to the
MySQL documentation](https://dev.mysql.com/doc/).*
"""
import nepc
cnx, cursor = nepc.connect(local=True)

# %% [markdown]
"""
The nepc database happens to have the Phelps N$_2$ dataset
organized into a 
[nepc "Model"](https://nepc.readthedocs.io/en/latest/?badge=latest#nepc.nepc.Model).
"""
n2_phelps = nepc.Model(cursor, "phelps")


# %% [markdown]
"""
nepc.Model.cs is a list of nepc.CS objects.
"""
n2_phelps.cs

# %% [markdown]
"""
nepc.CS objects have dictionaries of metadata and data. How do they
compare to the LXCat text files.
"""
n2_phelps.cs[15].metadata

# %%
n2_phelps.cs[15].data


# %% [markdown]
"""
The `nepc.Model` class has a `summary` method that provides
a stylized pandas DataFrame of some of the data and some
of the metadata.
"""
n2_phelps.summary()

# %% [markdown]
"""
The stylized pandas dataframe from `nepc.Model.summary` isn't as 
useful in an interactive code block as it is in a Jupyter notebook. 

Fortunately, we have some example Jupyter notebooks in 
[nepc_cs](https://github.com/NRL-Plasma-Physics-Division/nepc_cs), 
the repo for managing data within the NEPC MySQL database in use
at NRL.

***We keep the open source nepc framework separate from curation
scripts and data for a production NEPC database.***
"""
# %% [markdown]
"""
And there's a `nepc.Model.plot` method that uses matplotlib under
the hood.
"""
n2_phelps.plot(units_sigma=1E-20, process='excitation',
               plot_param_dict = {'linewidth':.8}, 
               #xlim_param_dict = {'left': 0.01, 'right': 120.0}, 
               ylog=True, xlog=True, max_plots=40, width=8, height=4) 

# %%
n2_phelps.plot(units_sigma=1E-20, process='excitation_v',
               plot_param_dict = {'linewidth':.8}, 
               #xlim_param_dict = {'left': 0.01, 'right': 120.0}, 
               ylog=True, xlog=True, max_plots=40, width=8, height=4)

