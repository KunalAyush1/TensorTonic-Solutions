import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    x = np.asarray(x)
    p = np.asarray(p)

    xp = x * p

    expected_value = float(np.sum(xp))

    return expected_value
    pass