__author__ = "github.com/wardsimon"
__version__ = "0.0.1"

from easyTemplateLib.Engines.calculatorTemplate import CalculatorTemplate


class Calculator2(CalculatorTemplate):
    name = "BFGS"

    def __init__(self, obj, x=None, gtol=1e-05, eps=1.4901161193847656e-08, maxiter=None):
        super().__init__(obj, x)
        self._store = {'gtol': gtol,
                       'eps': eps,
                       'maxiter': maxiter
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

