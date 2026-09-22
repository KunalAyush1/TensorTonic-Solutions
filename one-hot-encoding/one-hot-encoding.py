import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    # Write code here
    y = np.asarray(y)
    k = num_classes
    if num_classes is None:
        k = np.max(y) + 1
    
    one_hot_encoded_matrix = np.zeros((len(y), k))

    for i in range(len(y)):
        one_hot_encoded_matrix[i][y[i]] = 1.0

    return one_hot_encoded_matrix
