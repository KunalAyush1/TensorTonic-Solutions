import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    X = np.asarray(x)
    Y = np.asarray(y)

    distance = float((np.abs(X - Y)).sum())
    return distance
    pass