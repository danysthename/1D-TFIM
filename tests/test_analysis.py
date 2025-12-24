import pytest
import sys
import os
from unittest.mock import patch, MagicMock

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import analysis.sweep_energy
import analysis.inspect_wavefunction
import analysis.entanglement_entropy

@patch('matplotlib.pyplot.show')
def test_sweep_energy_runs(mock_show):
    """Test that sweep_energy.py runs without error and generates data."""
    # Mock sys.argv to simulate command line arguments
    test_args = ["sweep_energy.py", "--N", "2", "--J", "1.0", "--steps", "5"]
    with patch.object(sys, 'argv', test_args):
        # Run main
        analysis.sweep_energy.main()
    
    # Check if data file was created
    data_path = os.path.join(os.path.dirname(__file__), '../data/gs_data_N2.npz')
    assert os.path.exists(data_path)
    mock_show.assert_called_once()

@patch('matplotlib.pyplot.show')
def test_inspect_wavefunction_runs(mock_show):
    """Test that inspect_wavefunction.py runs without error (reads data)."""
    # Ensure data exists first (test_sweep_energy_runs should ideally run first, 
    # but we can rely on existing data or run it here if needed)
    data_path = os.path.join(os.path.dirname(__file__), '../data/gs_data_N2.npz')
    if not os.path.exists(data_path):
        analysis.sweep_energy.main()
        
    analysis.inspect_wavefunction.main()

@patch('matplotlib.pyplot.show')
def test_analysis_entanglement_runs(mock_show):
    """Test that analysis/entanglement_entropy.py runs without error."""
    # This script loads gs_data_N10.npz.
    data_path = os.path.join(os.path.dirname(__file__), '../data/gs_data_N10.npz')
    
    if os.path.exists(data_path):
        analysis.entanglement_entropy.main()
        mock_show.assert_called_once()
    else:
        pytest.skip(f"Data file {data_path} not found")
