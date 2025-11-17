import numpy as np

def intercept_solver(x_mean, y_mean, gradient):

    intercept = y_mean - gradient * x_mean

    return intercept