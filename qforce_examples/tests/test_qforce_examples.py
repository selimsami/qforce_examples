"""
Unit and regression test for the qforce_examples package.
"""

# Import package, test suite, and other packages as needed
import os
import pytest

from qforce_examples import Orca_default, Gaussian_default

@pytest.mark.parametrize("test_input", [Orca_default, Gaussian_default])
def test_files_exist(test_input):
    """Test if the files do exist."""
    for key in test_input:
        assert os.path.isfile(test_input[key])
