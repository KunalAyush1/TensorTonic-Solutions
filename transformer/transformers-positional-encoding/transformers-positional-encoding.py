import numpy as np

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model).
    """
    a = np.arange(seq_len)
    b = np.arange(d_model)
    a = a[:, None]
    c = base ** (((b // 2) * 2 ) / d_model)
            
    angle = a / c
    mask = b % 2 == 0 
    encoding = np.empty_like(angle, dtype=float)

    encoding[:, mask] = np.sin(angle[:, mask])
    encoding[:, ~mask] = np.cos(angle[:, ~mask])

    return encoding