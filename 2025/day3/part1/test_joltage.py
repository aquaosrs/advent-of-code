import unittest
from joltage import processJoltage


class TestJoltage(unittest.TestCase):
    
    def test_case_1(self):
        """In 987654321111111, you can make the largest joltage possible, 98, 
        by turning on the first two batteries."""
        result = processJoltage("987654321111111")
        self.assertEqual(result, 98)
    
    def test_case_2(self):
        """In 811111111111119, you can make the largest joltage possible by 
        turning on the batteries labeled 8 and 9, producing 89 jolts."""
        result = processJoltage("811111111111119")
        self.assertEqual(result, 89)
    
    def test_case_3(self):
        """In 234234234234278, you can make 78 by turning on the last two 
        batteries (marked 7 and 8)."""
        result = processJoltage("234234234234278")
        self.assertEqual(result, 78)
    
    def test_case_4(self):
        """In 818181911112111, the largest joltage you can produce is 92."""
        result = processJoltage("818181911112111")
        self.assertEqual(result, 92)
    
    def test_case_5(self):
        """Test case with long string of digits - should produce 44, not 34."""
        result = processJoltage("2221334423231421112242332222123422224122214133424132222222212433123124322322222322232231213242244314")
        self.assertEqual(result, 44)


if __name__ == "__main__":
    unittest.main()
