import numpy as np

def impute_missing(X: list, strategy: str = "mean") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as X.
    """
    # Write code here

    X = np.asarray(X)

    if X.ndim == 1:
        if strategy == "mean":
            mean = np.nanmean(X)
            X[np.isnan(X)] = mean
        else:
            median = np.nanmedian(X)
            X[np.isnan(X)] = median

    else:
        if strategy == "mean":
            column_mean = np.nanmean(X, axis = 0)
            column_mean = np.nan_to_num(column_mean, nan=0.0)
            nan_matrix = np.isnan(X)
            for i in range(X.shape[0]):
                for j in range(X.shape[1]):
                    if nan_matrix[i][j] == True:
                        X[i][j] = column_mean[j]

        else:
            column_median = np.nanmedian(X, axis = 0)
            column_median = np.nan_to_num(column_median, nan=0.0)
            nan_matrix = np.isnan(X)
            for i in range(X.shape[0]):
                for j in range(X.shape[1]):
                    if nan_matrix[i][j] == True:
                        X[i][j] = column_median[j]


    return X
            
                    
        

    