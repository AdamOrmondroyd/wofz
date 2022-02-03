from cobaya.prior import Prior
from pypolychord.priors import UniformPrior, SortedUniformPrior

# I don't think I should have to import priors from polychord here. What I need to do
# is finish working on linf, so I have a general prior that I can apply here to w(z),
# and be able to use for other parameters, because inevitably w won't be the one that
# I end up investigating


class DarkLinfPrior(Prior):
    pass
