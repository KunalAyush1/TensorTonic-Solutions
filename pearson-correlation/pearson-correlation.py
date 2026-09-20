import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    X = np.asarray(X)

    Xc = X - np.mean(X, axis=0)

    cov_matrix = (Xc.T @ Xc) / (X.shape[0] - 1)

    pearson_correlation_matrix = np.zeros(
        (X.shape[1], X.shape[1])
    )

    for i in range(X.shape[1]):
        for j in range(X.shape[1]):

            std_i = np.std(X[:, i], ddof=1)
            std_j = np.std(X[:, j], ddof=1)

            if std_i == 0 or std_j == 0:
                pearson_correlation_matrix[i, j] = np.nan
            else:
                pearson_correlation_matrix[i, j] = (
                    cov_matrix[i, j] / (std_i * std_j)
                )

    return pearson_correlation_matrix