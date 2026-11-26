import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    X = np.asarray(X,dtype=float)
    center = X - np.mean(X,axis=0)
    cov = center.T @ center / (X.shape[0]-1)
    standard_deviation = np.sqrt(np.diag(cov))
    dem = np.outer(standard_deviation,standard_deviation)
    with np.errstate(divide="ignore",invalid="ignore"):
        return cov / dem