import numpy as np

def hinge_loss(y_true: list, y_score: list, margin: float = 1.0, reduction: str = "mean") -> float:
    """
    Returns the loss as a float.
    """
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)

    ys = margin - (y_true * y_score)

    for i in range(len(ys)):
        if ys[i] < 0:
            ys[i] = 0.0

    param = 0.0

    if reduction == "mean":
        param = float(np.mean(ys))
    else:
        param = float(np.sum(ys))

    return param
    