import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    X = np.asarray(X)
    Xc = X - np.mean(X, axis = 0)

    cov_matrix = ((Xc.T) @ (Xc)) / (X.shape[0] - 1)

    return cov_matrix