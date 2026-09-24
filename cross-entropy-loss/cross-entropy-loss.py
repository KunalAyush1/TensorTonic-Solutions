import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Returns the mean multiclass cross-entropy loss as a Python float.
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    l = np.zeros(len(y_true))


    for i in range(len(y_true)):
        l[i] = -np.log(y_pred[i][y_true[i]])

    

    loss = float(np.mean(l))

    return loss