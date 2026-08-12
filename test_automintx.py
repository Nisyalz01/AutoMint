# test_automintx.py
"""
Tests for AutoMintX module.
"""

import unittest
from automintx import AutoMintX

class TestAutoMintX(unittest.TestCase):
    """Test cases for AutoMintX class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AutoMintX()
        self.assertIsInstance(instance, AutoMintX)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AutoMintX()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
