import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    X = np.asarray(x)
    Y = np.asarray(y)

    d = np.sqrt(((Y-X)**2).sum())
    return d
    pass