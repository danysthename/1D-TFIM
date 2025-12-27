"""
Firstly define a range of h values to sweep over
Then for each h value, build the Hamiltonian and compute the ground state energy and wavefunction
finally plot the energy vs h and store the E_0 and psi0 for later use.
"""
import numpy as np
import sys
import os
import matplotlib.pyplot as plt

# Ensure we can import from the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ed.hamiltonian import gen_hamiltonian
from ed.ground_state import ground_state


def sweep_energy(N, J, h_values):
    """
    Sweep transverse field h and compute ground state energy and wavefunction.
    
    Args:
        N (int): Number of spins.
        J (float): Coupling constant.
        h_values (np.ndarray): Array of transverse field values.
        
    Returns:
        tuple: (energies, wavefunctions) lists.
    """
    energies = []
    wavefunctions = []
    
    for h in h_values:
            H = gen_hamiltonian(N, J, h)
            E0, psi0 = ground_state(H)
            
            energies.append(E0)
            wavefunctions.append(psi0)
    
    return energies, wavefunctions


import argparse

def main():
    parser = argparse.ArgumentParser(description="Sweep transverse field for 1D TFIM.")
    parser.add_argument("--N", type=int, default=2, help="Number of spins")
    parser.add_argument("--J", type=float, default=1.0, help="Coupling constant")
    parser.add_argument("--h_min", type=float, default=0.0, help="Minimum h value")
    parser.add_argument("--h_max", type=float, default=2.0, help="Maximum h value")
    parser.add_argument("--steps", type=int, default=20, help="Number of h steps")
    
    args = parser.parse_args()
    
    N = args.N
    J = args.J
    h_values = np.linspace(args.h_min, args.h_max, args.steps)
    
    print(f"Running sweep for N={N}, J={J}, h=[{args.h_min}, {args.h_max}] ({args.steps} steps)")
    
    energies, wavefunctions = sweep_energy(N, J, h_values)
    
    plt.plot(h_values, energies, 'o-')
    plt.xlabel("Transverse field h")
    plt.ylabel("Ground-state energy E0")
    plt.title(f"TFIM ground-state energy (N = {N})")
    plt.grid(True)
    plt.show()
    
    # Save data for later use
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    os.makedirs(data_dir, exist_ok=True)
    data_path = os.path.join(data_dir, f'gs_data_N{N}.npz')
    np.savez(data_path, h=h_values, energies=energies, states=wavefunctions)
    print(f"Data saved to {data_path}")


if __name__ == "__main__":
    main()