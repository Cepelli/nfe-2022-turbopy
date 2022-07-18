import pytest
from particle_system_c import *


def test_default_particle_is_an_electron():
    electron1 = Particle()
    assert electron1.particle_type == 'electron'
    assert electron1.charge == -1.602176634E-19 * ureg.coulomb
    assert electron1.mass == 9.10938356E-31 * ureg.kilogram
    assert electron1.spin == '1/2'

    
def test_we_can_create_a_positron():
    positron1 = Particle(particle_type='positron')
    assert positron1.particle_type == 'positron'
    assert positron1.charge == 1.602176634E-19 * ureg.coulomb
    assert positron1.mass == 9.10938356E-31 * ureg.kilogram
    assert positron1.spin == '1/2'


def test_we_can_create_a_proton():
    proton1 = Particle(particle_type='proton')
    assert proton1.particle_type == 'proton'
    assert proton1.charge == 1.602176634E-19 * ureg.coulomb
    assert proton1.mass == 1.672621898E-27 * ureg.kilogram
    assert proton1.spin == '1/2'


def test_we_cannot_create_a_neutron():
    with pytest.raises(NotImplementedError):
        neutron1 = Particle(particle_type='neutron')

