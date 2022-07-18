from pint import UnitRegistry
from abc import ABC

ureg = UnitRegistry()

electron_mass = 9.10938356E-31 * ureg.kilogram
electron_charge = -1.602176634E-19 * ureg.coulomb
proton_mass = 1.672621898E-27 * ureg.kilogram


class Particle(ABC):
    def __init__(self, id, particle_type):
        self.id = id
        self.particle_type = particle_type
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


class Electron(Particle):
    def __init__(self, id):
        super().__init__(id, particle_type='electron')


class Positron(Particle):
    def __init__(self, id):
        super().__init__(id, particle_type='positron')


class Proton(Particle):
    def __init__(self, id):
        super().__init__(id, particle_type='proton')