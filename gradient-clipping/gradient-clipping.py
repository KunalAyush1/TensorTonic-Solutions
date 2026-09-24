import numpy as np

def clip_gradients(g: list, max_norm: float) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as g.
    """
    # Write code here
    g = np.asarray(g)

    g_norm = np.sqrt(np.sum(g ** 2))

    if g_norm > max_norm:
        g = g * max_norm / g_norm

    return g