# %% [markdown]
'''
# Example of refactoring code

In this example, I will first create a simple turboPy "app" which generates a radial profile. Basically, it will evaluate a function on the grid. Depending on the configuration, different functional forms can be chosen, and different paramter values can be used.

I'll then show how changing "switch" statements in multiple places can lead to bugs, and also make code hard to extend.

Finally, I'll show how refactoring the code to use the "factory pattern" helps to avoid the bugs, and makes the code easier to understand, test, and extend.
'''

# %%
from os import stat
import numpy as np
import turbopy
import matplotlib.pyplot as plt

# %%
# Use the factory pattern to choose between different options for profiles
def ProfileFactory(profile, **parameters):
    # the "switch" has to go somewhere, so put it here so it's only in one place
    if profile == 'gaussian':
        return GaussianProfile(**parameters)
    else:
        raise NotImplementedError(f"Unknown profile type: {profile}")

class GaussianProfile:
    def __init__(self, radius, amplitude, **kwargs) -> None:
        self.radius = radius
        self.amplitude = amplitude

    def profile(self, r):
        return self.amplitude * np.exp(-(r / self.radius) ** 2)

    def ddr_profile(self, r):
        return -2 * (r / self.radius ** 2) * self.amplitude \
            * np.exp(-(r / self.radius) ** 2)

class BennettProfile:
    def __init__(self, radius, amplitude, **kwargs) -> None:
        self.radius = radius
        self.amplitude = amplitude

    def profile(self, r):
        return self.amplitude * 1.0 / (1.0 + (r / self.radius) ** 2) ** 2

    def ddr_profile(self, r):
        return -4 * self.amplitude * (1.0 + (r / self.radius) ** 2) ** -3 \
            * (r / self.radius ** 2)

class RadialProfile(turbopy.PhysicsModule):
    def __init__(
            self, 
            owner: turbopy.Simulation, 
            input_data: dict):
        super().__init__(owner, input_data)
        self._input_data = input_data
        
        # Attributes to share
        self.profile = owner.grid.generate_field(1)
        self.ddr_profile = owner.grid.generate_field(1)

        # Call functions which actually set the profile
        profile = ProfileFactory(**input_data)
        self.set_profile(profile)
        self.set_ddr_profile(profile)

    def exchange_resources(self):
        self.publish_resource({
                "RadialProfile:f": self.profile,
                "RadialProfile:dfdr": self.ddr_profile
            })

    def set_profile(self, profile):
        '''Set the functional form of the radial profile'''
        self.profile[:] = profile.profile(self._owner.grid.r)

    def set_ddr_profile(self, profile):
        self.ddr_profile[:] = profile.ddr_profile(self._owner.grid.r)

    def update(self):
        pass

# Add the new module to the registry
turbopy.PhysicsModule.register('RadialProfile', RadialProfile)

# %%

problem_config = {
    'Grid':
    {'N': 50, 'max': 1, 'min': 0},
'Clock':
{'dt': 1, 'end_time': 1, 'print_time': False, 'start_time': 0},
'PhysicsModules':
{
    'RadialProfile':
    {
        'profile': 'gaussian',
        'amplitude': 1,
        'radius': 0.5,
    },
}, 
'Diagnostics':
{
'directory': './',
'histories': [{'filename': 'history.nc',
                'interval': 1,
                'traces': [{'coords': ['grid'],
                            'long_name': 'Profile',
                            'name': 'RadialProfile:f',
                            'units': 'A'},
                           {'coords': ['grid'],
                            'long_name': 'Derivative',
                            'name': 'RadialProfile:dfdr',
                            'units': 'A/m'},
                            ]
                }]
}
}


sim = turbopy.Simulation(problem_config)
sim.run()
ds = sim.diagnostics[0]._traces

# %%
plt.figure()
plt.subplot(2,1,1)
plt.plot(ds['r'], ds['RadialProfile:f'][:])
plt.xlabel('Position [m]')
plt.ylabel('Profile [A]')
plt.grid()

plt.subplot(2,1,2)
plt.plot(ds['r'], ds['RadialProfile:dfdr'][:])
plt.xlabel('Position [m]')
plt.ylabel('Derivative [A/m]')
plt.grid()

plt.tight_layout()
plt.show()

# %%
problem_config['PhysicsModules']['RadialProfile']['profile'] = 'bennett'

sim = turbopy.Simulation(problem_config)
sim.run()
ds = sim.diagnostics[0]._traces

plt.figure()
plt.subplot(2,1,1)
plt.plot(ds['r'], ds['RadialProfile:f'][:])
plt.xlabel('Position [m]')
plt.ylabel('Profile [A]')
plt.grid()

plt.subplot(2,1,2)
plt.plot(ds['r'], ds['RadialProfile:dfdr'][:])
plt.xlabel('Position [m]')
plt.ylabel('Derivative [A/m]')
plt.grid()

plt.tight_layout()
plt.show()
