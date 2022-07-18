# %%
from pyquante2 import basisset,rhf,rohf,h2,h2o,lih,oh,co,ch4,he
from pyquante2.graphics import contourplot
import matplotlib.pyplot as plt
import pandas as pd
import time

# %% [markdown]
"""
To use the `rhf` or `rohf` method in pyquante2, we need to define
a basis set and a molecule.

We want to store all of our data, including input and ouput,
in a pandas dataframe, so let's create variables to store our input
parameters.
"""

basissets = ['sto3g', '6-31g', '6-31g**']
molecules = {'h2': h2, 
             'he': he,
             'lih': lih, 
             'oh': oh, 
             'h2o': h2o,
             'ch4': ch4, 
             'co': co}

# %% [markdown]
"""
We want to run pyquante2 for all combinations of the above basis
sets and molecules.
"""
basis_mol = [[i, j] for i in basissets for j in molecules.keys()]
data = pd.DataFrame(basis_mol, columns=['basisset', 'molecule'])

# %%
data

# %% [markdown]
"""
So now, we can use the strings in the `molecule` column of `data` as
keys in our `molecules` dictionary. (Later, we'll use the strings in
the `basisset` column to create our pyquante2 basis set object.)
"""

# %%
h2.html

# %%
molecules[data['molecule'][0]].atoms

# %% [markdown]
"""
## Example RHF calculation
"""
bfs = basisset(lih, '6-31g**')
solver = rhf(lih, bfs)
solver.converge()

# %%
bfs.shells

# %%
solver.orbe

# %%
solver.orbs

# %%
contourplot.contourplot('xy', lih, solver.orbs[1], bfs)

# %%
contourplot.contourplot('yz', lih, solver.orbs[1], bfs)

# %%
contourplot.contourplot('xz', lih, solver.orbs[1], bfs)

# %% [markdown]
"""
When do we use `rhf` versus `rohf`?

RHF: restricted Hartree-Fock, valid for closed shell molecules (no unpaired electrons)

ROHF: restricted open-shell Hartree-Fock, valid for open shell molecules (unpaired electrons)
"""

for key, value in molecules.items():
    print(f"{key:3} | name: {value.name:10} mult: {value.multiplicity}")

# %%
energy = []
t = []
for index, contents in data.iterrows():
    start_time = time.time()
    molec = molecules[contents['molecule']]
    bfs = basisset(molec, contents['basisset'])
    solver = rohf(molec, bfs) if molec.multiplicity > 1 else rhf(molec, bfs)
    energy += [solver.converge()[-1]]
    t += [time.time() - start_time]
data['energy'] = pd.Series(energy)
data['t'] = pd.Series(t)

# %%j
data

# %%
data.pivot(index='molecule', columns='basisset', values='energy')

# %%
data.pivot(index='molecule', columns='basisset', values='t')

# %%
print(f"Total time for all calculations: {data['t'].sum():.2f} s") 

# %%
data.groupby('basisset').sum()['t'].sort_values()

# %%
basisset(h2, 'sto3g').shells

# %%
basisset(h2, '6-31g**').shells
# %%

basisset(lih, '6-31g**').shells

# %%
basisset(ch4, '6-31g**').shells

# %%
len(basisset(ch4, '6-31g**').shells)

# %%
def numshells(molecule_name, basisset_name):
    return len(basisset(molecules[molecule_name], basisset_name).shells) 

# %%
data['numshells'] = data.apply(lambda row: numshells(row.molecule, row.basisset), axis=1)

# %%
data

# %%
data.plot(x='numshells', y='t', kind='scatter')

# %%
molecule_groups = data.groupby('molecule')

# %%
for name, group in molecule_groups:
    plt.plot(group.numshells, group.t, marker='o',
             linestyle='--', markersize=5, label=name)
plt.legend()

# %%
for name, group in molecule_groups:
    plt.plot(group.numshells, group.energy, marker='o',
             linestyle='--', markersize=5, label=name)
plt.legend()

# %%
solver.converged

# %%
energy = []
t = []
converged = []
for index, contents in data.iterrows():
    start_time = time.time()
    molec = molecules[contents['molecule']]
    bfs = basisset(molec, contents['basisset'])
    solver = rohf(molec, bfs) if molec.multiplicity > 1 else rhf(molec, bfs)
    energy += [solver.converge()[-1]]
    t += [time.time() - start_time]
    converged.append(solver.converged)
data['energy'] = pd.Series(energy)
data['t'] = pd.Series(t)
data['converged'] = pd.Series(converged)

# %%
data
