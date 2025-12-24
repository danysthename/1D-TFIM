import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# Ensure we can import from the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ed.utils import entanglement_entropy


def main():
    data_path = os.path.join(os.path.dirname(__file__), '../data/gs_data_N10.npz')
    data = np.load(data_path, allow_pickle=True)

    entropy_values = []

    for index in range(len(data['h'])):
        psi0 = data['states'][index]
        psi_matrix = psi0.reshape(32, 32)
        U, s, Vh = np.linalg.svd(psi_matrix)
        entropy = entanglement_entropy(s)
        entropy_values.append(entropy)

    plt.plot(data['h'], entropy_values, 'o-')
    plt.xlabel("Transverse field h")
    plt.ylabel("Entanglement Entropy S")
    plt.title("Entanglement Entropy vs Transverse Field (N = 10)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
