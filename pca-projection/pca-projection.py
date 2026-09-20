import numpy as np

def pca_projection(X: list, k: int) -> list:
    """
    Returns the centered data projected onto the top components.
    """
    X = np.asarray(X)

    Xc = X - np.mean(X, axis=0)

    cov_matrix = (Xc.T @ Xc) / (X.shape[0] - 1)

    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    idx = np.argsort(eigenvalues)[::-1]

    top_idx = idx[:k]

    W = eigenvectors[:,top_idx]

    X_proj = Xc @ W

    return X_proj

    

    

    