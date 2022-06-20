# from ctypes import c_double

import numpy as np
from cobaya import Theory
from linf import AdaptiveLinf, Linf


class DarkLinf(Theory):
    """
    Abstract base class for linf w(a).

    Requires additional class attribute params, which needs to be
    ordered in the correct structure for a linf, and definition of
    self.linf needs to be added to
    """

    num_as = 10000
    amin = 1e-10
    atoday = 1

    def wofa(self, theta):
        a = np.logspace(np.log10(self.amin), np.log10(self.atoday), self.num_as)
        w = self.linf(a, theta)

        return a, w

    def calculate(self, state, want_derived=True, **params_values_dict):
        theta = np.array([params_values_dict[p] for p in self.params.keys()])
        a, w = self.wofa(theta)
        state["dark_energy"] = {
            "a": a,
            "w": w,
        }

    def get_dark_energy(self):
        return self.current_state["dark_energy"]


class AdaptiveDarkLinf(DarkLinf):

    params = {
        "N": None,
        "w0": None,
        "a1": None,
        "w1": None,
        "a2": None,
        "w2": None,
        "a3": None,
        "w3": None,
        "a4": None,
        "w4": None,
        "a5": None,
        "w5": None,
        "a6": None,
        "w6": None,
        "a7": None,
        "w7": None,
        "w8": None,
    }

    def __init__(self, *args, **kwargs):

        self.linf = AdaptiveLinf(self.amin, self.atoday)
        super().__init__(*args, **kwargs)


class VanillaDarkLinf(DarkLinf):
    def __init__(self, *args, **kwargs):

        self.linf = Linf(self.amin, self.atoday)
        super().__init__(*args, **kwargs)


# TODO: see if I can just put the params in the constructor to be
# defined with a for loop


class Vanilla1(VanillaDarkLinf):

    params = {
        "w8": None,
    }


class Vanilla2(VanillaDarkLinf):

    params = {
        "w0": None,
        "w8": None,
    }


class Vanilla3(VanillaDarkLinf):

    params = {
        "w0": None,
        "a1": None,
        "w1": None,
        "w8": None,
    }


class Vanilla4(VanillaDarkLinf):

    params = {
        "w0": None,
        "a1": None,
        "w1": None,
        "a2": None,
        "w2": None,
        "w8": None,
    }


class Vanilla5(VanillaDarkLinf):

    params = {
        "w0": None,
        "a1": None,
        "w1": None,
        "a2": None,
        "w2": None,
        "a3": None,
        "w3": None,
        "w8": None,
    }


class Vanilla6(VanillaDarkLinf):

    params = {
        "w0": None,
        "a1": None,
        "w1": None,
        "a2": None,
        "w2": None,
        "a3": None,
        "w3": None,
        "a4": None,
        "w4": None,
        "w8": None,
    }


class Vanilla7(VanillaDarkLinf):

    params = {
        "w0": None,
        "a1": None,
        "w1": None,
        "a2": None,
        "w2": None,
        "a3": None,
        "w3": None,
        "a4": None,
        "w4": None,
        "a5": None,
        "w5": None,
        "w8": None,
    }


class Vanilla8(VanillaDarkLinf):

    params = {
        "w0": None,
        "a1": None,
        "w1": None,
        "a2": None,
        "w2": None,
        "a3": None,
        "w3": None,
        "a4": None,
        "w4": None,
        "a5": None,
        "w5": None,
        "a6": None,
        "w6": None,
        "w8": None,
    }


class Vanilla9(VanillaDarkLinf):

    params = {
        "w0": None,
        "a1": None,
        "w1": None,
        "a2": None,
        "w2": None,
        "a3": None,
        "w3": None,
        "a4": None,
        "w4": None,
        "a5": None,
        "w5": None,
        "a6": None,
        "w6": None,
        "a7": None,
        "w7": None,
        "w8": None,
    }
