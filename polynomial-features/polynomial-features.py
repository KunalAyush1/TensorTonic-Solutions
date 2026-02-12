import numpy as np
def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    values = np.array(values)
    rows = values.shape[0]
    cols = degree

    pol_features = np.zeros((rows, cols+1))
    for i in range(rows):
        for j in range(cols + 1):
            pol_features[i][j] = values[i]**j

    return pol_features.tolist()

    # Write code here