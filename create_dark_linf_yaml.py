import numpy as np
import yaml


def create_wofa_yaml(
    output_filepath,
    Nmax,
    amin=0.1,
    atoday=1.0,
    wmin=-1,
    wmax=-0.5,
    num_as = 10000,
    adaptive=True,
    N=None,
    input_filepath="dark_linf_template.yaml",
    nlive=None,
):
    with open(input_filepath) as in_file:
        yaml_dict = yaml.load(in_file, Loader=yaml.FullLoader)

        yaml_dict["sampler"] = {"polychord": {}}
        if nlive:
            yaml_dict["sampler"]["polychord"]["nlive"] = nlive

        yaml_dict["theory"]["camb"]["external_wa"] = True

        if adaptive:
            # TODO: remember the lower bound will need changing to 0 for w(z)
            yaml_dict["params"]["N"] = {"prior": [1, Nmax + 1], "latex": "N"}
            yaml_dict["theory"]["dark_linf.AdaptiveDarkLinf"] = {
                "python_path": "src/",
                "num_as": num_as,
                "amin": amin,
                "atoday": atoday,
            }
            for i in np.arange(Nmax):

                yaml_dict["params"][f"w{i}"] = {
                    "prior": [wmin, wmax],
                    "latex": f"w{i}"
                }
        else:
            yaml_dict["theory"][f"dark_linf.Vanilla{N}"] = {
                "python_path": "src/",
                "num_as": num_as,
                "amin": amin,
                "atoday": atoday,
            }
            for i in np.concatenate((np.arange(N - 1), [Nmax - 1])):

                yaml_dict["params"][f"w{i}"] = {
                    "prior": [wmin, wmax],
                    "latex": f"w{i}",
                }

        # w nodes

        # a nodes
        # if 4 or more nodes (i.e. 2 or more internal nodes),
        # they need to be sorted

        if adaptive:
            N = Nmax

        if N >= 4:
            sorted_prior_arguments = ""
            sorted_prior_expression = ""

        for i in np.arange(N - 2) + 1:
            yaml_dict["params"][f"a{i}"] = {
                "prior": [amin, atoday],
                "latex": f"a{i}",
            }

            if N >= 4:
                sorted_prior_arguments += f"a{i}"
                if i < N - 2:
                    sorted_prior_arguments += ", "
                if i > 1:
                    sorted_prior_expression += " < "

                sorted_prior_expression += f"a{i}"

        if N >= 4:
            sorted_prior = (
                f"lambda {sorted_prior_arguments}: np.log({sorted_prior_expression})"
            )
            yaml_dict["prior"] = {"sorted_prior": sorted_prior}

        out_file = open(output_filepath, "w")
        yaml.dump(yaml_dict, out_file)


if __name__ == "__main__":
    amin, atoday = 0.1, 1
    wmin, wmax = -1, -0.5

    Nmax = 9

    create_wofa_yaml(
        "generated_yamls/linf_adaptive.yaml",
        Nmax,
        amin,
        atoday,
        wmin,
        wmax,
        adaptive=True,
    )
    for i in np.arange(Nmax) + 1:
        create_wofa_yaml(
            f"generated_yamls/linf_vanilla_{i}.yaml",
            Nmax,
            amin,
            atoday,
            wmin,
            wmax,
            adaptive=False,
            N=i,
        )
