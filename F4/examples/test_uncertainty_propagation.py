import pytest
from pytest import approx as approx
from uncertainty_propagation import *

def test_addition_uncertainty():
    # approx is used with floats
    assert addition_uncertainty((2.0, 0.01), (3.0, 0.03), True) == approx((5.0, 0.0316), abs=1e-4)

