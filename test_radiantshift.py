# test_radiantshift.py
"""
Tests for RadiantShift module.
"""

import unittest
from radiantshift import RadiantShift

class TestRadiantShift(unittest.TestCase):
    """Test cases for RadiantShift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RadiantShift()
        self.assertIsInstance(instance, RadiantShift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RadiantShift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
