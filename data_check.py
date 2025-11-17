def data_checker(data):

    if data.ndim != 2 or data.shape[1] != 2:
        raise ValueError("Input must be an N x 2 NumPy array.")