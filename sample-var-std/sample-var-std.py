import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    x = np.asarray(x)

    sum_sq = np.sum((x - np.mean(x)) ** 2)

    var  = float(sum_sq / (x.shape[0] - 1))

    dev = float(np.sqrt(var))


    return {"variance": var, "standard_deviation": dev}
    
    