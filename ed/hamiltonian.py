"""
Use the operators defined in operators.py to generate the Hamiltonian for the 1D TFIM
"""
import numpy as np
import scipy
from scipy.sparse import csr_matrix, kron
from scipy.sparse.linalg import eigsh
from functools import reduce
from .operators import sx, sz, I, kron_list


"""Generate the Hamiltonian for the 1D TFIM"""
def gen_hamiltonian(N, J, h):

    H = csr_matrix((2**N, 2**N))  # initialize as zero sparse matrix
    
    # X terms
    for i in range(N):
        op_list1 = [I] * N
        op_list1[i] = sx
        H = H - h * kron_list(op_list1)
    
    # ZZ terms
    for i in range(N - 1):
        op_list2 = [I] * N
        op_list2[i] = sz
        op_list2[i + 1] = sz
        H = H - J * kron_list(op_list2)

    return H