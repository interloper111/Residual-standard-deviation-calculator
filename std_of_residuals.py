import numpy as np

def residual_std_solver(residuals):

    N=residuals.size
    if N <=2:
        raise ValueError("You need more than 2 x values for this to work buddy")
    residual_std = np.sqrt(np.sum(residuals ** 2) / (N-2))

    return residual_std