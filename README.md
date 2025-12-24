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

### Running Analysis
The analysis script `sweep_energy.py` now supports command-line arguments for flexibility.

**Basic Run (default N=2):**
```bash
python analysis/sweep_energy.py
```

**Custom Parameters:**
Run a sweep for $N=10$ spins with 50 steps:
```bash
python analysis/sweep_energy.py --N 10 --steps 50
```

**Available Arguments:**
- `--N`: Number of spins (default: 2)
- `--J`: Coupling constant (default: 1.0)
- `--h_min`: Minimum transverse field (default: 0.0)
- `--h_max`: Maximum transverse field (default: 2.0)
- `--steps`: Number of field steps (default: 20)

This will:
1.  Compute the ground state energy for the specified parameters.
2.  Display a plot of Energy vs. Field.
3.  Save the results to `data/gs_data_N{N}.npz`.

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
