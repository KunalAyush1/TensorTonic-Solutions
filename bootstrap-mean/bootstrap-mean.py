import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    x = np.asarray(x)

    n = len(x)

    rng = np.random.default_rng(seed)

    sample_mean = np.zeros(n_bootstrap)

    for i in range(n_bootstrap):
        sample = rng.choice(x, size=n, replace=True)
        sample_mean[i] = np.mean(sample)

    b_mean = float(np.mean(sample_mean))

    alpha = ( 1 - ci) / 2

    lower = float(np.quantile(sample_mean, alpha))
    upper = float(np.quantile(sample_mean, ( 1 - alpha)))

    return {"bootstrap_mean": b_mean, "lower": lower, "upper": upper}