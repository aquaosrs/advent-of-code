import unittest
import sys
import os
import reports


class TestReports(unittest.TestCase):
    
    def test_safe_decreasing_by_1_or_2(self):
        """Test: 7 6 4 2 1 - Safe because the levels are all decreasing by 1 or 2"""
        result = reports.isRowSafe("7 6 4 2 1")
        self.assertTrue(result)
    
    def test_unsafe_increase_of_5(self):
        """Test: 1 2 7 8 9 - Unsafe because 2 7 is an increase of 5"""
        result = reports.isRowSafe("1 2 7 8 9")
        self.assertFalse(result)
    
    def test_unsafe_decrease_of_4(self):
        """Test: 9 7 6 2 1 - Unsafe because 6 2 is a decrease of 4"""
        result = reports.isRowSafe("9 7 6 2 1")
        self.assertFalse(result)
    
    def test_unsafe_mixed_direction(self):
        """Test: 1 3 2 4 5 - Unsafe because 1 3 is increasing but 3 2 is decreasing"""
        result = reports.isRowSafe("1 3 2 4 5")
        self.assertFalse(result)
    
    def test_unsafe_no_change(self):
        """Test: 8 6 4 4 1 - Unsafe because 4 4 is neither an increase or a decrease"""
        result = reports.isRowSafe("8 6 4 4 1")
        self.assertFalse(result)
    
    def test_safe_increasing_by_1_2_or_3(self):
        """Test: 1 3 6 7 9 - Safe because the levels are all increasing by 1, 2, or 3"""
        result = reports.isRowSafe("1 3 6 7 9")
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
