import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A)
    rows = A.shape[0]
    cols = A.shape[1]
    a_transpose = np.zeros((cols, rows))
    # Write code here
    for i in range(rows):
        for j in range(cols):
           a_transpose[j][i] = A[i][j]
    
    return a_transpose
