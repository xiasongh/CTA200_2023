import numpy as np

def iterate(c, threshold=4, max_iter=100):
    z = 0
    for i in range(max_iter):
        z = z*z + c
        if np.abs(z) > threshold:
            return i
    return 0