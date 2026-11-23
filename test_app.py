#!/usr/bin/env python3
"""
Unit tests for the simple calculator app
"""

import unittest
from app import add_numbers, multiply_numbers

class TestCalculator(unittest.TestCase):
    
    def test_add_numbers(self):
        """Test addition function"""
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)
    
    def test_multiply_numbers(self):
        """Test multiplication function"""
        self.assertEqual(multiply_numbers(3, 4), 12)
        self.assertEqual(multiply_numbers(-2, 3), -6)
        self.assertEqual(multiply_numbers(0, 5), 0)

if __name__ == '__main__':
    unittest.main()

    def test_subtract_numbers(self):
        """Test subtraction function"""
        self.assertEqual(subtract_numbers(5, 3), 2)
        self.assertEqual(subtract_numbers(0, 5), -5)
        self.assertEqual(subtract_numbers(-2, -3), 1)

    def test_divide_numbers(self):
        """Test division function"""
        self.assertEqual(divide_numbers(10, 2), 5.0)
        self.assertEqual(divide_numbers(9, 3), 3.0)
        with self.assertRaises(ValueError):
            divide_numbers(5, 0)
