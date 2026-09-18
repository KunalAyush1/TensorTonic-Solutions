import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    
    A = np.asarray(A)
    trace = 0.0

    if A.ndim != 1:
        for i in range(len(A[0])):
                    trace += A[i][i]
    else:
        trace = A[0]

    return trace
        