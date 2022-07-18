from particle_system_e import *
import numpy as np


def test_we_can_create_an_electron():
    electron1 = Electron(1)
    assert electron1.particle_type == 'electron'
    assert electron1.property.charge == -1.602176634E-19 * ureg.coulomb
    assert electron1.property.mass == 9.10938356E-31 * ureg.kilogram
    assert electron1.property.spin == '1/2'

    
def test_we_can_create_a_positron():
    positron1 = Positron(1)
    assert positron1.particle_type == 'positron'
    assert positron1.property.charge == 1.602176634E-19 * ureg.coulomb
    assert positron1.property.mass == 9.10938356E-31 * ureg.kilogram
    assert positron1.property.spin == '1/2'


def test_we_can_create_a_proton():
    proton1 = Proton(1)
    assert proton1.particle_type == 'proton'
    assert proton1.property.charge == 1.602176634E-19 * ureg.coulomb
    assert proton1.property.mass == 1.672621898E-27 * ureg.kilogram
    assert proton1.property.spin == '1/2'


def test_we_can_create_a_system_of_three_protons():
    x = 0.5E-9 * ureg.meter
    z = np.sqrt((1.0E-9 * ureg.meter)**2 - x**2)
    proton1 = Proton(id=1, position=( x, 0, 0))
    proton2 = Proton(id=2, position=(-x, 0, 0)) 
    proton3 = Proton(id=3, position=( 0, 0, z))
    system = System([proton1, proton2, proton3])
    assert len(system) == 3
    assert system.particles[0].particle_type == 'proton'
    assert system.particles[1].particle_type == 'proton'
    assert system.particles[2].particle_type == 'proton'
    assert np.abs(system.potential_energy() - 6.665E-19 * ureg.joule) < 0.001 * ureg.joule
