from pint import UnitRegistry
from abc import ABC, abstractmethod
import numpy as np
import itertools

ureg = UnitRegistry()

electron_mass = 9.10938356E-31 * ureg.kilogram
electron_charge = -1.602176634E-19 * ureg.coulomb
proton_mass = 1.672621898E-27 * ureg.kilogram


class Particle(ABC):
    def __init__(self, id, position, particle_type):
        self.id = id
        self.particle_type = particle_type
        self.position = position
        self.property = Property(particle_type)
    

class Property:
    def __init__(self, particle_type):
        _particle_properties = {'electron':{'mass': electron_mass,
                                            'charge': electron_charge,
                                            'spin': '1/2'},
                                'positron':{'mass': electron_mass,
                                            'charge': -1.0 * electron_charge,
                                            'spin': '1/2'},
                                'proton':  {'mass': proton_mass,
                                            'charge': -1.0 * electron_charge,
                                            'spin': '1/2'}}
        self.mass = _particle_properties[particle_type]['mass']
        self.charge = _particle_properties[particle_type]['charge']
        self.spin = _particle_properties[particle_type]['spin']


class System:
    def __init__(self, particle_list):
        self.particles = particle_list

    def potential_energy(self):
        pe = 0.0 * ureg.joule
        for (particle_a, particle_b) in itertools.combinations(self.particles, 2):
            r = np.sqrt(
                (particle_a.position[0] - particle_b.position[0])**2 +
                (particle_a.position[1] - particle_b.position[1])**2 +
                (particle_a.position[2] - particle_b.position[2])**2)
            ke = 8.9875517873681764E9 * ureg.newton * ureg.meter**2 / ureg.coulomb**2
            pe += ke * particle_a.property.charge * particle_b.property.charge / r
        return pe

    def __len__(self):
        return len(self.particles)


class Electron(Particle):
    def __init__(self, id, position=(0.0 * ureg.meter, 0.0 * ureg.meter, 0.0 * ureg.meter)):
        super().__init__(id, position, particle_type='electron')


class Positron(Particle):
    def __init__(self, id, position=(0.0 * ureg.meter, 0.0 * ureg.meter, 0.0 * ureg.meter)):
        super().__init__(id, position, particle_type='positron')


class Proton(Particle):
    def __init__(self, id, position=(0.0 * ureg.meter, 0.0 * ureg.meter, 0.0 * ureg.meter)):
        super().__init__(id, position, particle_type='proton')