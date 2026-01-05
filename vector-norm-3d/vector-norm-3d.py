import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    # Your code here
    X = np.asarray(v)
    square = X * X
    norm = np.zeros(X.shape[0],dtype=float)
    if X.ndim == 1:
        norm = np.sqrt(square.sum())
    else:
        for i in range(X.shape[0]):
            norm[i] = np.sqrt(square[i].sum())
    return norm
    pass