from pint import UnitRegistry


ureg = UnitRegistry()

electron_mass = 9.10938356E-31 * ureg.kilogram
electron_charge = -1.602176634E-19 * ureg.coulomb
proton_mass = 1.672621898E-27 * ureg.kilogram
electron_spin = '1/2'


class Particle:
    def __init__(self, particle_type='electron'):
        self.particle_type = particle_type
        if self.particle_type == 'electron':
            self.mass = electron_mass
            self.charge = electron_charge
            self.spin = electron_spin
        elif self.particle_type == 'positron':
            self.mass = electron_mass
            self.charge = -1.0 * electron_charge
            self.spin = electron_spin
        elif self.particle_type == 'proton':
            self.mass = proton_mass
            self.charge = -1.0 * electron_charge
            self.spin = electron_spin
        else:
            raise NotImplementedError(f"particle type {self.particle_type} "
                                       "not implemented")
