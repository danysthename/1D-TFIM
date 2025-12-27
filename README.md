# 1D-TFIM

Exact diagonalization and approximate ground-state methods for the 1D Transverse Field Ising Model (TFIM).

## Overview

This repository contains Python implementations for analyzing the 1D Transverse Field Ising Model. It includes:
- Exact Diagonalization (ED) to find the ground state energy and wavefunction.
- Construction of Hamiltonians for arbitrary system sizes.
- Analysis scripts to sweep parameters and visualize results.

The Hamiltonian used is:
$$ H = -J \sum_{i} Z_i Z_{i+1} - h \sum_i X_i $$
where:
- $J$ is the ferromagnetic coupling constant.
- $h$ is the transverse magnetic field strength.
- $X_i, Z_i$ are Pauli matrices acting on site $i$.

## Project Structure

```
1D-TFIM/
├── analysis/           # Scripts for running parameter sweeps and analysis
├── data/               # Directory for storing output data
├── ed/                 # Core logic for Exact Diagonalization
│   ├── ground_state.py # Function to compute ground state
│   ├── hamiltonian.py  # Function to generate sparse Hamiltonian
│   └── operators.py    # Basic Pauli operators
├── notes/              # Research notes and logs
├── tests/              # Unit tests
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/yourusername/1D-TFIM.git
    cd 1D-TFIM
    ```

2.  Create and activate a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

    **Alternative: using Conda**
    ```bash
    conda env create -f environment.yml
    conda activate 1d-tfim
    ```

## Usage

### 1. Run Energy Sweep
First, generate the ground state data for a specific $N$:
```bash
python analysis/sweep_energy.py --N 10
```
This saves the results to `data/gs_data_N10.npz`.

### 2. Analyze Entanglement Entropy
Visualize the phase transition by plotting Entanglement Entropy vs. Field:
```bash
python analysis/entanglement_entropy.py --N 10
```

### 3. Inspect Wavefunction Structure
Visualize the probability amplitudes $|c_i|^2$ to see the underlying structure and symmetry:
```bash
python analysis/inspect_wavefunction.py --N 10 --h 2.0
```

### 4. Scaling Analysis (Why MPS?)
Demonstrate the motivation for Matrix Product States by comparing RAM usage (exponential) vs. Entanglement Entropy (area law):
```bash
python analysis/why_mps.py
```
This script runs a scan over $N=[2, 4, ..., 12]$ and saves a plot to `analysis/scaling_analysis.png`.

### Using the Library
You can use the `ed` module in your own scripts:

```python
from ed.hamiltonian import gen_hamiltonian
from ed.ground_state import ground_state

# Parameters
N = 4
J = 1.0
h = 0.5

# Compute
H = gen_hamiltonian(N, J, h)
E0, psi0 = ground_state(H)

print(f"Ground State Energy: {E0}")
```

## Testing

To run the unit tests:

```bash
pytest tests/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
