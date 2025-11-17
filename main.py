import numpy as np
from data_check import data_checker
from least_squares_gradient import gradient_solver
from least_squares_intercept import intercept_solver
from residuals import residuals_solver
from std_of_residuals import residual_std_solver

data = np.genfromtxt("data.txt",dtype='float',delimiter=',',skip_header=0)
data_checker(data)

x = data[:, 0]
y = data[:, 1]

x_mean = x.mean()
y_mean = y.mean()

gradient = gradient_solver(x, y, x_mean, y_mean)
intercept = intercept_solver(x_mean, y_mean, gradient)

residuals = residuals_solver(x, y, gradient, intercept)

print(residual_std_solver(residuals))