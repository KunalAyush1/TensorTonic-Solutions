import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    a = np.asarray(matrix)
    if norm_type == "l1":
        if axis == 1:
            sum = np.sum(np.abs(a),axis=1, keepdims=True)
            sum = np.where(sum == 0, 1,sum)
            return a / sum
        elif axis == 0:
            sum = np.sum(np.abs(a),axis=0, keepdims=True)
            sum = np.where(sum == 0, 1,sum)
            return a / sum
        else:
            sum = np.sum(np.abs(a), keepdims=True)
            sum = np.where(sum == 0, 1,sum)
            return a / sum

    elif norm_type == "l2":
        if axis == 1:
            sq = a * a
            sum = np.sum(sq, axis=1, keepdims=True)
            sqrt = np.sqrt(sum)
            sqrt = np.where(sqrt == 0, 1,sqrt)
            return a / sqrt
        elif axis == 0:
            sq = a * a
            sum = np.sum(sq, axis=0, keepdims=True)
            sqrt = np.sqrt(sum)
            sqrt = np.where(sqrt == 0, 1,sqrt)
            return a / sqrt
        else:
            sq = a * a
            sum = np.sum(sq, keepdims=True)
            sqrt = np.sqrt(sum)
            sqrt = np.where(sqrt == 0, 1,sqrt)
            return a / sqrt
    elif norm_type == "max":
        if axis == 1:
            maxi = np.max(a, axis=1, keepdims=True)
            maxi = np.where(maxi == 0, 1,maxi)
            return a / maxi
        elif axis == 0:
            maxi = np.max(a, axis=0, keepdims=True)
            maxi = np.where(maxi == 0, 1,maxi)
            return a / maxi
        else:
            maxi = np.max(a, keepdims=True)
            maxi = np.where(maxi == 0, 1,maxi)
            return a / maxi