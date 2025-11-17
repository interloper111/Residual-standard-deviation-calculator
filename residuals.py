def residuals_solver(x, y, gradient, intercept):

    y_predicted= gradient * x + intercept
    residuals = y - y_predicted

    return residuals