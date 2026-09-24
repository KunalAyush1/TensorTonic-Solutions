import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)

    w = np.zeros(X.shape[1])
    b = 0.0
    p = 0.0
    l = 0.0

    for i in range(steps):
        p = _sigmoid(X @ w + b)
        l = -np.mean((y * np.log(p)) + (1 - y) * np.log(1 - p))
        grad_w = X.T @ (p - y) / len(y)
        grad_b = np.mean(p - y)

        w = w - lr * grad_w
        b = b - lr * grad_b

    return w, b
        
        
        