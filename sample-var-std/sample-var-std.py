import numpy as np

def sample_var_std(x: list) -> dict:
    x = np.asarray(x,dtype=float)
    center = x - np.mean(x)
    var = float(np.sum(center ** 2) / (x.size - 1))
    s_d = float(np.sqrt(var))
    return {"variance":var,"standard_deviation":s_d}