import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    a = np.asarray(a)
    b = np.asarray(b)
   
    a_sq = np.sqrt(np.sum(a * a))
    b_sq = np.sqrt(np.sum(b * b))

    if a_sq == 0 or b_sq == 0:
        return 0.0

    

    return float(np.dot(a,b)/(a_sq * b_sq))