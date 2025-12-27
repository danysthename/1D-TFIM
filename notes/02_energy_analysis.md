# Ground State Energy & Wavefunction Analysis
 
## 1. Ground State Energy Computation
For a fixed system size N, we sweep the transverse field h and compute the ground-state energy using sparse Exact Diagonalization. The ground-state wavefunction is stored at each field value to enable subsequent analysis.

- **Observation**: The energy varies smoothly with h, decreasing as field strength increases.
- **Key Insight**: The most rapid changes occur near h approx 1, signaling the finite-size precursor of the quantum critical point.
- **Limitation**: Energy alone is insufficient. It reduces trivially as -h increases, hiding the complex structural changes happening in the state. We need a deeper metric.

## 2. Insufficient Methods: Probability Amplitudes
To understand the state better, we inspected the raw wavefunction probability amplitudes |ci|^2 for a specific h.

**Wavefunction Structure:**
We observed two key features in the distribution:
1.  **Pairwise Symmetry**: Amplitudes appear in identical pairs. This captures the system's global Z2 symmetry (spin-flip invariance), confirming the simulation's physical correctness.
2.  **Non-Uniform Distribution**: A few configurations dominate while the tail drops off rapidly.

**Conclusion**: The state has significant "structure" (it is not random). However, raw amplitudes do not quantify *how* the spatial parts of the system are connected.

## 3. The Need for Entanglement Entropy
Since local Hamiltonian interactions lead to a global wavefunction, we need to understand how spatial divisions affect the system.

- **Why Entanglement Entropy?**: It serves as a single metric that compresses the Schmidt coefficients (singular values) of the state.
- **Significance**: Singular values quantify the correlation between subsystem partitions. By tracking the entropy, we measure the "complexity" of these correlations, which is the key to understanding the Phase Transition that energy plots missed.
