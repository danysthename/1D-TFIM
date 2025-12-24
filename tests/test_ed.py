import pytest
import numpy as np
import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ed.hamiltonian import gen_hamiltonian
from ed.ground_state import ground_state

def test_hamiltonian_shape():
    """Test if Hamiltonian has correct shape 2^N x 2^N"""
    N = 3
    H = gen_hamiltonian(N, J=1.0, h=0.5)
    assert H.shape == (2**N, 2**N)

def test_hamiltonian_hermitian():
    """Test if Hamiltonian is Hermitian"""
    N = 3
    H = gen_hamiltonian(N, J=1.0, h=0.5)
    # Check if H - H^dagger is close to zero
    diff = H - H.conj().transpose()
    assert np.allclose(diff.toarray(), 0, atol=1e-10)

def test_ground_state_single_spin():
    """
    Test ground state energy for N=1.
    H = -h * X
    Eigenvalues of X are +1 and -1.
    So eigenvalues of -h*X are -h and +h.
    Ground state energy should be -|h|.
    """
    N = 1
    J = 0.0 # Interaction doesn't matter for N=1
    h = 2.0
    
    H = gen_hamiltonian(N, J, h)
    E0, psi0 = ground_state(H)
    
    assert np.isclose(E0, -abs(h), atol=1e-5)

def test_ground_state_exact_limit():
    """
    Test N=2 limit case.
    For h=0, H = -J * Z1*Z2.
    Eigenvalues of Z1*Z2 are +1, -1.
    Ground state energy should be -|J|.
    """
    N = 2
    J = 1.0
    h = 0.0
    
    H = gen_hamiltonian(N, J, h)
    E0, psi0 = ground_state(H)
    
    assert np.isclose(E0, -abs(J), atol=1e-5)
