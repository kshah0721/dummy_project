import numpy as np

def get_square(x: np.ndarray) -> np.ndarray:
    """Returns the square of an array/list of numbers
    Parameters
    ----------
    x: np.ndarray
        Input array
    """
    assert isinstance(x, (np.ndarray, list)), "Not write type of input"
    return x**2
