import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    X=np.asarray(X,dtype=float)
    center = X - np.mean(X,axis=0)
    return center.T @ center / (X.shape[0]-1)