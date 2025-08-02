# test_nextmotion.py
"""
Tests for NextMotion module.
"""

import unittest
from nextmotion import NextMotion

class TestNextMotion(unittest.TestCase):
    """Test cases for NextMotion class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NextMotion()
        self.assertIsInstance(instance, NextMotion)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NextMotion()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
