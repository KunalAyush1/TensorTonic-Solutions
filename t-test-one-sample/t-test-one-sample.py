import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    x = np.asarray(x)

    sum = float(0.0)

    n = len(x)

    for i in range(n):
        sum += ((x[i] - np.mean(x)) ** 2)

    s = float(np.sqrt(sum / (n - 1)))


    t = float(((np.mean(x) - mu0) * np.sqrt(n)) / s)


    return t