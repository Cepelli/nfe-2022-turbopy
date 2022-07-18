from particle_system_d import *


def test_we_can_create_an_electron():
    electron1 = Electron(id=1)
    ureg = UnitRegistry()
    assert electron1.particle_type == 'electron'
    assert electron1.id == 1
    assert electron1.property.charge == -1.602176634E-19 * ureg.coulomb
    assert electron1.property.mass == 9.10938356E-31 * ureg.kilogram
    assert electron1.property.spin == '1/2'

    
def test_we_can_create_a_positron():
    positron1 = Positron(id=1)
    ureg = UnitRegistry()
    assert positron1.particle_type == 'positron'
    assert positron1.id == 1
    assert positron1.property.charge == 1.602176634E-19 * ureg.coulomb
    assert positron1.property.mass == 9.10938356E-31 * ureg.kilogram
    assert positron1.property.spin == '1/2'


def test_we_can_create_a_proton():
    proton1 = Proton(id=1)
    ureg = UnitRegistry()
    assert proton1.particle_type == 'proton'
    assert proton1.id == 1
    assert proton1.property.charge == 1.602176634E-19 * ureg.coulomb
    assert proton1.property.mass == 1.672621898E-27 * ureg.kilogram
    assert proton1.property.spin == '1/2'
