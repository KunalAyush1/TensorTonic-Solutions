import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)

    if y_pred.shape == y_true.shape:
        SE = ((y_pred - y_true)**2).sum()
        MSE = SE/y_pred.shape[0]
        return MSE
    else:
        return None
    pass
