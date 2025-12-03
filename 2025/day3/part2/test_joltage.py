import unittest
from joltage import processJoltage


class TestJoltage(unittest.TestCase):
    
    def test_case_1(self):
        """In 987654321111111, the largest joltage can be found by turning on 
        everything except some 1s at the end to produce 987654321111."""
        result = processJoltage("987654321111111")
        self.assertEqual(result, 987654321111)
    
    def test_case_2(self):
        """In the digit sequence 811111111111119, the largest joltage can be 
        found by turning on everything except some 1s, producing 811111111119."""
        result = processJoltage("811111111111119")
        self.assertEqual(result, 811111111119)
    
    def test_case_3(self):
        """In 234234234234278, the largest joltage can be found by turning on 
        everything except a 2 battery, a 3 battery, and another 2 battery near 
        the start to produce 434234234278."""
        result = processJoltage("234234234234278")
        self.assertEqual(result, 434234234278)
    
    def test_case_4(self):
        """In 818181911112111, the joltage 888911112111 is produced by turning 
        on everything except some 1s near the front."""
        result = processJoltage("818181911112111")
        self.assertEqual(result, 888911112111)
    

if __name__ == "__main__":
    unittest.main()
