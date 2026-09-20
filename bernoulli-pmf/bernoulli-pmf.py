import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    x = np.asarray(x)
    

    dist = np.zeros(x.shape[0])

    mean = float(p)
    var = float(p * (1 - p))

    for i in range(x.shape[0]):
        if x[i] == 0:
            dist[i] = 1 - p
        else:
            dist[i] = p
            
    


    return {"pmf": dist, "mean": mean, "variance": var}
            

    