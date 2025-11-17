import numpy as np

def gradient_solver(x, y, x_mean, y_mean):

    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)

    if denominator == 0:
        raise ZeroDivisionError("All x values are identical, maybe get some more results")

    gradient = numerator / denominator

    return gradient