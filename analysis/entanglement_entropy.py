"""
Compute the entanglement entropy for the ground state of the 1D TFIM.
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# Ensure we can import from the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ed.utils import entanglement_entropy


import argparse

def main():
    parser = argparse.ArgumentParser(description="Compute entanglement entropy for 1D TFIM.")
    parser.add_argument("--N", type=int, default=10, help="Number of spins")
    args = parser.parse_args()
    N = args.N

    data_path = os.path.join(os.path.dirname(__file__), f'../data/gs_data_N{N}.npz')
    
    if not os.path.exists(data_path):
        print(f"Error: Data file {data_path} not found. Run sweep_energy.py --N {N} first.")
        return

    data = np.load(data_path, allow_pickle=True)

    entropy_values = []

    for index in range(len(data['h'])):
        psi0 = data['states'][index]
        psi_matrix = psi0.reshape(2**(N//2), 2**(N - N//2)) # Dynamic reshaping
        U, s, Vh = np.linalg.svd(psi_matrix)
        entropy = entanglement_entropy(s)
        entropy_values.append(entropy)

    plt.plot(data['h'], entropy_values, 'o-')
    plt.xlabel("Transverse field h")
    plt.ylabel("Entanglement Entropy S")
    plt.title(f"Entanglement Entropy vs Transverse Field (N = {N})")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
