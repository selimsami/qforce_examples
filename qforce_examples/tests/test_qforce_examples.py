"""
Unit and regression test for the qforce_examples package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import qforce_examples


def test_qforce_examples_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "qforce_examples" in sys.modules
