import numpy as np
from scipy.sparse.linalg import eigsh


def ground_state(H):
    """
    Computes the ground state energy and wavefunction of a Hamiltonian.

    Args:
        H (scipy.sparse.csr_matrix): The Hamiltonian matrix.

    Returns:
        tuple: (E0, psi0) where E0 is the ground state energy and psi0 is the wavefunction.
    """
    #chose SA because we want the smallest eigenvalue (ground state energy)
    evals, evecs = eigsh(H, k=1, which='SA')

    E0 = evals[0]
    psi0 = evecs[:, 0]

    return E0, psi0
