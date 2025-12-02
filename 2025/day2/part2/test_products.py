import unittest
from products import processRange


class TestProducts(unittest.TestCase):
    
    def test_range_11_22(self):
        """11-22 still has two invalid IDs, 11 and 22."""
        result = processRange("11-22")
        self.assertEqual(len(result), 2)
        self.assertIn(11, result)
        self.assertIn(22, result)

    def test_range_95_115(self):
        """95-115 now has two invalid IDs, 99 and 111."""
        result = processRange("95-115")
        self.assertEqual(len(result), 2)
        self.assertIn(99, result)
        self.assertIn(111, result)

    def test_range_998_1012(self):
        """998-1012 now has two invalid IDs, 999 and 1010."""
        result = processRange("998-1012")
        self.assertEqual(len(result), 2)
        self.assertIn(999, result)
        self.assertIn(1010, result)

    def test_range_1188511880_1188511890(self):
        """1188511880-1188511890 still has one invalid ID, 1188511885."""
        result = processRange("1188511880-1188511890")
        self.assertEqual(len(result), 1)
        self.assertIn(1188511885, result)

    def test_range_222220_222224(self):
        """222220-222224 still has one invalid ID, 222222."""
        result = processRange("222220-222224")
        self.assertEqual(len(result), 1)
        self.assertIn(222222, result)

    def test_range_1698522_1698528(self):
        """1698522-1698528 still contains no invalid IDs."""
        result = processRange("1698522-1698528")
        self.assertEqual(len(result), 0)

    def test_range_446443_446449(self):
        """446443-446449 still has one invalid ID, 446446."""
        result = processRange("446443-446449")
        self.assertEqual(len(result), 1)
        self.assertIn(446446, result)

    def test_range_38593856_38593862(self):
        """38593856-38593862 still has one invalid ID, 38593859."""
        result = processRange("38593856-38593862")
        self.assertEqual(len(result), 1)
        self.assertIn(38593859, result)

    def test_range_565653_565659(self):
        """565653-565659 now has one invalid ID, 565656."""
        result = processRange("565653-565659")
        self.assertEqual(len(result), 1)
        self.assertIn(565656, result)

    def test_range_824824821_824824827(self):
        """824824821-824824827 now has one invalid ID, 824824824."""
        result = processRange("824824821-824824827")
        self.assertEqual(len(result), 1)
        self.assertIn(824824824, result)

    def test_range_2121212118_2121212124(self):
        """2121212118-2121212124 now has one invalid ID, 2121212121."""
        result = processRange("2121212118-2121212124")
        self.assertEqual(len(result), 1)
        self.assertIn(2121212121, result)


if __name__ == '__main__':
    unittest.main()
