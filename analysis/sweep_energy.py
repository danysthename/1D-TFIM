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


def main():
    # fix size
    N = 2
    J = 1.0
    
    h_values = np.linspace(0.0, 2.0, 20)
    
    energies, wavefunctions = sweep_energy(N, J, h_values)
    
    plt.plot(h_values, energies, 'o-')
    plt.xlabel("Transverse field h")
    plt.ylabel("Ground-state energy E0")
    plt.title(f"TFIM ground-state energy (N = {N})")
    plt.grid(True)
    plt.show()
    
    # Save data for later use
    data_path = os.path.join(os.path.dirname(__file__), '../data/gs_data_N2.npz')
    np.savez(data_path, h=h_values, energies=energies, states=wavefunctions)


if __name__ == "__main__":
    main()