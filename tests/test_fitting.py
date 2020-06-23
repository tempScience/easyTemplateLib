__author__ = "github.com/wardsimon"
__version__ = "0.0.1"

from easyTemplateLib.Objects.fitting import Model
import numpy as np

def f(x, m=1, c=2):
    return m*x + c


def test_model():
    m = Model(f)
    assert m.independent_vars == ['x']
    assert 'm' in m.param_names
    assert 'c' in m.param_names
    pars = m.make_params()
    assert 'm' in pars.keys()
    assert 'c' in pars.keys()
    assert pars['m'].value == 1
    assert pars['m'].vary is True
    assert pars['c'].value == 2
    assert pars['c'].vary is True

def test_fitting():
    m = Model(f)
    data =