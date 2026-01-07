import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    # Write code here
    x = np.asarray(X)
    mean1 = x.mean(axis = axis, keepdims=True)
    std1 = x.std(axis = axis, keepdims=True)
   

    z = np.asarray((x - mean1 )/np.maximum(eps,std1))
    return z 
    pass