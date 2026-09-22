import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    A = np.asarray(A)

    aug = np.concatenate((A, np.eye(len(A[0]))), axis=1)

    for i in range(len(A)):
        if aug[i, i] == 0:
            for k in range(i + 1, len(A)):
                if aug[k, i] != 0:
                    aug[[i, k]] = aug[[k, i]]
                    break
            else:
                return None

        aug[i, :] = aug[i, :] / aug[i, i]

        for k in range(len(A)):
            if k != i:
                aug[k, :] = aug[k, :] - aug[k, i] * aug[i, :]

    inv = aug[:, len(A):]

    return inv