import numpy as np
import sys
import os

# Ensure we can import from the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ed.utils import entanglement_entropy


def main():
    """
    Analyse the probability amplitudes of the ground state wavefunction obtained from sweep_energy.py.
    """
    data_path = os.path.join(os.path.dirname(__file__), '../data/gs_data_N2.npz')
    data = np.load(data_path, allow_pickle=True)
    print(data.files)

    target_h = 2.0
    index = np.argmin(np.abs(data['h'] - target_h))

    psi0 = data['states'][index]
    h_value = data['h'][index]

    print("inspecting wavefunction at h =", h_value)
    print("Wavefunction shape:", psi0.shape)

    probs = np.abs(psi0)**2
    print("sum of probabilities:", np.sum(probs))

    sorted_probs = np.sort(probs)[::-1]
    for i in range(psi0.shape[0]):
        print(sorted_probs[i])

    print("psi0 shape:", psi0.shape)
    print("norm:", np.sum(np.abs(psi0)**2))

    # Partition
    psi_matrix = psi0.reshape(2, 2)
    U, s, Vh = np.linalg.svd(psi_matrix)
    print("Singular values:", s)
    print("Sum of Schmidt coefficients (squared):", np.sum(s**2))

    print("Entanglement entropy:", entanglement_entropy(s))


if __name__ == "__main__":
    main()