# from ctypes import c_double

import numpy as np

# from camb.dark_energy import DarkEnergyPPF
from cobaya import Theory
from linf import AdaptiveLinf

a_min = 0
a_today = 1


# class DarkEnergyLinf(DarkEnergyPPF):

#     params = {
#         "N": None,
#         "w0": None,
#         "a1": None,
#         "w1": None,
#         "a2": None,
#         "w2": None,
#         "w3": None,
#     }

#     # what the heck are we actually meant to do here? I don't feel like this
#     # can possibly be the way given how they went on about putting so much
#     # effort into writing the python wrapper. Why does it lack clear instructions?
#     # I think the only clear reason for this can be that I'm barking up the wrong tree.
#     # someone must have tried a different model for dark energy at some point

#     def __init__(self, *args, **kwargs):
#         print("DarkEnergyLinf constructor")
#         return super().__init__(*args, **kwargs)

#     def set_params(self, N, w0, a1, w1, a2, w2, w3):
#         print("setting DarkEnergyLinf params")
#         self.N = N
#         self.w0 = w0
#         self.a1 = a1
#         self.w1 = w1
#         self.a2 = a2
#         self.w2 = w2
#         self.w3 = w3

#         self.linf = AdaptiveLinf(a_min, a_today)
#         theta = np.array([N, w0, a1, w1, a2, w2, w3])

#         # use linspace to fill w(a) so that cubic spline approximates linf
#         a = np.linspace(a_min, a_today)  # linspace
#         w = self.linf(a, theta)

#         self.use_tabulated_w = True
#         self.set_w_a_table(a, w)


class DarkEnergyLinfTheory(Theory):

    params = {
        "N": None,
        "w0": None,
        "a1": None,
        "w1": None,
        "a2": None,
        "w2": None,
        "w3": None,
    }

    # what the heck are we actually meant to do here? I don't feel like this
    # can possibly be the way given how they went on about putting so much
    # effort into writing the python wrapper. Why does it lack clear instructions?
    # I think the only clear reason for this can be that I'm barking up the wrong tree.
    # someone must have tried a different model for dark energy at some point

    def __init__(self, *args, **kwargs):
        print("DarkEnergyLinfTheory constructor")
        return super().__init__(*args, **kwargs)

    def calculate(self, state, want_derived=True, **params_values_dict):
        print("calculating DarkEnergyLinf")
        N, w0, a1, w1, a2, w2, w3 = [params_values_dict[p] for p in self.params.keys()]

        linf = AdaptiveLinf(a_min, a_today)
        theta = np.array([N, w0, a1, w1, a2, w2, w3])
        print(theta)

        # use linspace to fill w(a) so that cubic spline becomes linf (might want to increase number of points)
        # a = np.linspace(a_min, a_today)  # linspace
        a = np.array([a_min, a1, a2, a_today])
        w = linf(a, theta)
        state["dark_energy"] = {
            "a": a,
            "w": w,
        }  # working here (what elements does state have?)

    def get_dark_energy(self):
        print("getting DarkEnergyLinf")
        result = self.current_state["dark_energy"]
        print(f"result found:{result}")
        return result
