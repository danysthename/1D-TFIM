import numpy as np
from scipy.sparse import csr_matrix, kron
from functools import reduce

# Pauli matrices and Identity
sx = csr_matrix([[0, 1], [1, 0]],)
sz = csr_matrix([[1, 0], [0, -1]],)
I = csr_matrix(np.eye(2))

def kron_list(op_list):
    """
    Computes the Kronecker product of a list of operators.

    Args:
        op_list (list): List of sparse matrices.

    Returns:
        scipy.sparse.csr_matrix: The resulting Kronecker product.
    """
    return reduce(kron, op_list)






