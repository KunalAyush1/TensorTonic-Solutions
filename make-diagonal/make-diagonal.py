import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    v = np.asarray(v)
    diag = np.zeros((len(v), len(v)))


    for i in range(len(v)):
        diag[i][i] = v[i]


    return diag
        
               
    