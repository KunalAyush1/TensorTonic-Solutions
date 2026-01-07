import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    X = np.asarray(x)
    Y = np.asarray(y)

    dot_product = float(np.dot(X,Y))
    return dot_product
    pass