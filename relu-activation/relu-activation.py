import numpy as np

def relu(x):
   # atleast 1d function will convert the scalar to 1D thats the requirement here our solution was failing on this test case##
    X = np.atleast_1d(np.asarray(x, dtype=float))
    return np.maximum(0.0, X)
