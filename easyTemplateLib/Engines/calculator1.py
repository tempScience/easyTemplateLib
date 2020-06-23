__author__ = "github.com/wardsimon"
__version__ = "0.0.2"

from easyTemplateLib.Engines.calculatorTemplate import CalculatorTemplate


class Calculator1(CalculatorTemplate):
    name = "leastsq"

    def __init__(self, obj, x=None, xtol=1E-7, ftol=1E-7, Dfun=None):
        super().__init__(obj, x)
        self._store = {
            'xtol': xtol,
            'ftol': ftol,
            'Dfun': Dfun
        }
        for key in self._store.keys():
            setattr(
                self.__class__,
                key,
                property(self.__gitem(key), self.__sitem(key)),
            )

    def fit(self, data, **kwargs):
        if 'method' in kwargs.keys():
            raise AttributeError
        return self._fit(data, method=self.name, **self._store, **kwargs)
