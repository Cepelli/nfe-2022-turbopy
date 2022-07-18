import pytest
from particle_system_a import *


def test_we_can_create_an_electron():
    electron1 = Electron()
    assert electron1.particle_type == 'electron'
    assert electron1.charge == -1.602176634E-19 * ureg.coulomb
    assert electron1.mass == 9.10938356E-31 * ureg.kilogram
    assert electron1.spin == '1/2'

    
def test_we_can_create_a_positron():
    positron1 = Positron()
    assert positron1.particle_type == 'positron'
    assert positron1.charge == 1.602176634E-19 * ureg.coulomb
    assert positron1.mass == 9.10938356E-31 * ureg.kilogram
    assert positron1.spin == '1/2'

