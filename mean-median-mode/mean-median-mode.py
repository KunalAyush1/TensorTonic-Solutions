from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    x = np.asarray(x)

    mean = float(np.mean(x))
    median = float(np.median(x))

    counts = Counter(x)
    mode = float(counts.most_common(1)[0][0])

    return {"mean": mean, "median": median, "mode": mode}
        
        
  