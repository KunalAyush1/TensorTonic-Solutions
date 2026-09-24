import numpy as np

def kl_divergence(p: list, q: list, eps: float = 1e-12) -> float:
    """
    Returns the divergence as a float.
    """
    p = np.asarray(p)
    q = np.asarray(q)


    kl_div = float(np.sum(p[p > 0.0] * np.log(p[p > 0.0]/q[p > 0.0])))

    return kl_div