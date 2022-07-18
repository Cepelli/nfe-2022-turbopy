from pint import UnitRegistry


ureg = UnitRegistry()

electron_mass = 9.10938356E-31 * ureg.kilogram
electron_charge = -1.602176634E-19 * ureg.coulomb
electron_spin = '1/2'

class Electron:
    def __init__(self):
        self.particle_type = 'electron'
        self.mass = electron_mass
        self.charge = electron_charge
        self.spin = electron_spin
        

class Positron:
    def __init__(self):
        self.particle_type = 'positron'
        self.mass = electron_mass
        self.charge = -1.0 * electron_charge
        self.spin = electron_spin