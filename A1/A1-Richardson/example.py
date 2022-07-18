# %% [markdown]
'''
# Example of refactoring code

In this example, I will first create a simple turboPy "app" which generates a radial profile. Basically, it will evaluate a function on the grid. Depending on the configuration, different functional forms can be chosen, and different paramter values can be used.

I'll then show how changing "switch" statements in multiple places can lead to bugs, and also make code hard to extend.

Finally, I'll show how refactoring the code to use the "factory pattern" helps to avoid the bugs, and makes the code easier to understand, test, and extend.
'''

# %%
import numpy as np
import turbopy
import matplotlib.pyplot as plt

# %%
# Create a new class which defines a "profile"

class RadialProfile(turbopy.PhysicsModule):
    def __init__(
            self, 
            owner: turbopy.Simulation, 
            input_data: dict):
        super().__init__(owner, input_data)
        self._input_data = input_data
        
        # Set some parameters for the profile
        self.amplitude = input_data["amplitude"]
        self.radius = input_data["radius"]

        # Attributes to share
        self.profile = owner.grid.generate_field(1)
        self.ddr_profile = owner.grid.generate_field(1)

        # Call functions which actually set the profile
        self.set_profile(input_data["profile"])
        self.set_ddr_profile(input_data["profile"])

    def exchange_resources(self):
        self.publish_resource({
                "RadialProfile:f": self.profile,
                "RadialProfile:dfdr": self.ddr_profile
            })

    def set_profile(self, profile_type):
        '''Set the functional form of the radial profile'''
        profiles = {"gaussian": lambda r:
                    self.amplitude * np.exp(-(r / self.radius) ** 2),
                    "uniform": lambda r:
                    self.amplitude * (np.abs(r) < self.radius) / (np.pi * self.radius ** 2),
                    "bennett": lambda r:
                    self.amplitude * 1.0 / (1.0 + (r / self.radius) ** 2) ** 2,
                    "tent": lambda x:
                    (self.amplitude / self.radius) * np.piecewise(x,
                        [x < -self.radius,
                        (-self.radius <= x) & (x < 0),
                        (0 <= x) & (x < self.radius),
                        self.radius <= x],
                        [0, lambda x: x + self.radius,
                        lambda x: self.radius - x, 0]),
                    "ring": lambda x:
                    self.amplitude * np.piecewise(
                        x,
                        [x < -self.radius,
                         (-self.radius <= x) & (x < -(self.radius - 0.01)),
                         (-(self.radius - 0.01) <= x) & (x < self.radius - 0.01),
                         (self.radius - 0.01 <= x) & (x < self.radius),
                         (self.radius <= x)],
                        [0, 1, 0, 1, 0]),
                    }
        try:
            self.profile[:] = profiles[profile_type](self._owner.grid.r)
        except KeyError:
            raise KeyError("Unknown profile type: {0}".format(profile_type))

    def set_ddr_profile(self, profile_type):
        '''Set the form of the derivative of the profile'''
        profiles = {"gaussian": lambda r:
                    -2 * (r / self.radius ** 2) * self.amplitude * np.exp(-(r / self.radius) ** 2),
                    "tent": lambda x:
                    (self.amplitude / self.radius) * np.piecewise(x,
                        [x < -self.radius,
                        (-self.radius <= x) & (x < 0),
                        (0 <= x) & (x < self.radius),
                        self.radius <= x], [0, 1, -1, 0]),
                    "uniform": lambda x: 0 * x,
                    }
        try:
            self.ddr_profile[:] = profiles[profile_type](self._owner.grid.r)
        except KeyError:
            raise KeyError("Unknown profile type: {0}".format(profile_type))

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
