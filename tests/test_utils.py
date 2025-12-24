import pytest
import numpy as np
import sys
import os
from scipy.sparse import csr_matrix

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ed.utils import entanglement_entropy
from ed.operators import kron_list, sx, sz, I

def test_kron_list():
    """Test Kronecker product of list of operators."""
    # I (x) I should be identity of size 4x4
    op_list = [I, I]
    res = kron_list(op_list)
    assert res.shape == (4, 4)
    assert np.allclose(res.toarray(), np.eye(4))
    
    # sx (x) I
    # sx = [[0, 1], [1, 0]]
    # I = [[1, 0], [0, 1]]
    # Result should be [[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]]
    op_list2 = [sx, I]
    res2 = kron_list(op_list2)
    expected = np.array([
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 1, 0, 0]
    ])
    assert np.allclose(res2.toarray(), expected)

def test_entanglement_entropy_pure_state():
    """Entropy of a pure state (singular value 1) should be 0."""
    s = np.array([1.0, 0.0])
    S = entanglement_entropy(s)
    assert np.isclose(S, 0.0)

def test_entanglement_entropy_maximally_mixed():
    """
    Entropy of maximally mixed state of 2 qubits.
    Singular values are [1/sqrt(2), 1/sqrt(2)].
    S = - sum p_i log(p_i), where p_i = s_i^2 = 1/2.
    S = - (0.5 * ln(0.5) + 0.5 * ln(0.5)) = - ln(0.5) = ln(2)
    """
    s = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
    S = entanglement_entropy(s)
    expected = np.log(2)
    assert np.isclose(S, expected)
