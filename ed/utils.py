import numpy as np

def entanglement_entropy(s):
    """
    Computes the entanglement entropy from singular values.

    Args:
        s (np.ndarray): Array of singular values.

    Returns:
        float: The von Neumann entanglement entropy.
    """
    entropy = 0.0
    for val in s:
        if val > 1e-12:
            entropy -= (val**2) * np.log(val**2)
    return entropy
