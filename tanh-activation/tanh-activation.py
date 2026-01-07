import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    X = np.atleast_1d(np.asarray(x, dtype=float))
    tanh = (np.exp(X) - np.exp(-X)) / (np.exp(X) + np.exp(-X))
    return tanh
    pass