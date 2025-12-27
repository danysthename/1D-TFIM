import numpy as np
import sys
import os

# Ensure we can import from the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ed.utils import entanglement_entropy


import argparse
import matplotlib.pyplot as plt

def main():
    """
    Analyse the probability amplitudes of the ground state wavefunction.
    """
    parser = argparse.ArgumentParser(description="Inspect wavefunction amplitudes.")
    parser.add_argument("--N", type=int, default=10, help="Number of spins")
    parser.add_argument("--h", type=float, default=2.0, help="Target field value h")
    args = parser.parse_args()
    
    N = args.N
    target_h = args.h

    data_path = os.path.join(os.path.dirname(__file__), f'../data/gs_data_N{N}.npz')
    if not os.path.exists(data_path):
        print(f"Error: Data file {data_path} not found. Run sweep_energy.py --N {N} first.")
        return

    data = np.load(data_path, allow_pickle=True)

    # Find the index closest to the target h
    index = np.argmin(np.abs(data['h'] - target_h))
    
    psi0 = data['states'][index]
    h_value = data['h'][index]

    print(f"Inspecting wavefunction for N={N} at h={h_value:.4f}")
    
    probs = np.abs(psi0)**2
    print("Sum of probabilities:", np.sum(probs))

    # Sort for visualization if N is large
    sorted_probs = np.sort(probs)[::-1]
    
    # Text interactions
    print("Top 10 Probabilities:")
    for i in range(min(10, len(sorted_probs))):
        print(f"{i}: {sorted_probs[i]:.6f}")

    # Plotting
    plt.figure(figsize=(10, 6))
    
    # We plot the sorted probabilities to see the distribution structure
    plt.plot(sorted_probs, 'o-', markersize=4, label=f'h={h_value:.2f}')
    plt.yscale('log')
    plt.xlabel("Basis Index (Sorted by Amplitude)")
    plt.ylabel("Probability $|c_i|^2$ (Log Scale)")
    plt.title(f"Wavefunction Amplitudes (N={N}, h={h_value:.2f})")
    plt.grid(True, which="both", ls="--")
    plt.legend()
    
    plt.show() # Show the interactive plot
    
    output_file = os.path.join(os.path.dirname(__file__), 'wavefunction_probs.png')
    plt.savefig(output_file)
    print(f"Plot saved to: {output_file}")


if __name__ == "__main__":
    main()