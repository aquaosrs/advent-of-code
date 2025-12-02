import unittest
from io import StringIO
import sys
import dial


class TestDial(unittest.TestCase):
    def setUp(self):
        """Reset the dial before each test"""
        dial.currentNumber = 0
        dial.currentTimesWePassedZero = 0
        dial.currentTimesWeStopAtZero = 0
    
    def test_turnDial_forward(self):
        """Test turning the dial forward"""
        dial.currentNumber = 0
        result = dial.turnDial(10)
        self.assertEqual(result, 10)
    
    def test_turnDial_backward(self):
        """Test turning the dial backward"""
        dial.currentNumber = 10
        result = dial.turnDial(-5)
        self.assertEqual(result, 5)
    
    def test_turnDial_wrap_around(self):
        """Test that the dial wraps around at 99"""
        dial.currentNumber = 95
        result = dial.turnDial(10)
        self.assertEqual(result, 5)
    
    def test_turnDial_wrap_around_backward(self):
        """Test that the dial wraps around backward"""
        dial.currentNumber = 5
        result = dial.turnDial(-10)
        self.assertEqual(result, 95)
    
    def test_turnDialFromString_left(self):
        """Test turning left from string"""
        dial.currentNumber = 50
        result = dial.turnDialFromString("L68")
        self.assertEqual(result, 82)
    
    def test_turnDialFromString_right(self):
        """Test turning right from string"""
        dial.currentNumber = 0
        result = dial.turnDialFromString("R48")
        self.assertEqual(result, 48)
    
    def test_expected_output_sequence(self):
        """Test the complete sequence matches expected output"""
        expected_output = """The dial starts by pointing at 50.
The dial is rotated L68 to point at 82.
The dial is rotated L30 to point at 52.
The dial is rotated R48 to point at 0.
The dial is rotated L5 to point at 95.
The dial is rotated R60 to point at 55.
The dial is rotated L55 to point at 0.
The dial is rotated L1 to point at 99.
The dial is rotated L99 to point at 0.
The dial is rotated R14 to point at 14.
The dial is rotated L82 to point at 32.
"""
        
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Run the main logic
        dial.currentNumber = 50
        print(f"The dial starts by pointing at {dial.currentNumber}.")
        stepsList = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
        for steps in stepsList:
            newNumber = dial.turnDialFromString(steps)
            print(f"The dial is rotated {steps} to point at {newNumber}.")
        
        # Restore stdout
        sys.stdout = sys.__stdout__
        
        # Compare output
        actual_output = captured_output.getvalue()
        self.assertEqual(actual_output, expected_output)
    
    def test_individual_steps(self):
        """Test each individual step in the sequence"""
        dial.currentNumber = 50
        
        # L68 from 50 -> 82 (50 - 68 = -18, wraps to 82)
        result = dial.turnDialFromString("L68")
        self.assertEqual(result, 82, "L68 from 50 should be 82")
        self.assertEqual(dial.currentTimesWePassedZero, 1, "Should pass 0 once when wrapping backward")
        self.assertEqual(dial.currentTimesWeStopAtZero, 0, "Should not stop at 0")
        
        # L30 from 82 -> 52 (82 - 30 = 52, no wrap)
        result = dial.turnDialFromString("L30")
        self.assertEqual(result, 52, "L30 from 82 should be 52")
        self.assertEqual(dial.currentTimesWePassedZero, 1, "Should not pass 0")
        self.assertEqual(dial.currentTimesWeStopAtZero, 0, "Should not stop at 0")
        
        # R48 from 52 -> 0 (52 + 48 = 100, wraps to 0)
        result = dial.turnDialFromString("R48")
        self.assertEqual(result, 0, "R48 from 52 should be 0")
        self.assertEqual(dial.currentTimesWePassedZero, 2, "Should pass 0 once when wrapping forward")
        self.assertEqual(dial.currentTimesWeStopAtZero, 1, "Should stop at 0 for the first time")
        
        # L5 from 0 -> 95 (0 - 5 = -5, wraps to 95)
        result = dial.turnDialFromString("L5")
        self.assertEqual(result, 95, "L5 from 0 should be 95")
        self.assertEqual(dial.currentTimesWePassedZero, 3, "Should pass 0 once when wrapping backward")
        self.assertEqual(dial.currentTimesWeStopAtZero, 1, "Stop at 0 count unchanged")
        
        # R60 from 95 -> 55 (95 + 60 = 155, wraps to 55)
        result = dial.turnDialFromString("R60")
        self.assertEqual(result, 55, "R60 from 95 should be 55")
        self.assertEqual(dial.currentTimesWePassedZero, 4, "Should pass 0 once more when wrapping forward")
        self.assertEqual(dial.currentTimesWeStopAtZero, 1, "Stop at 0 count unchanged")
        
        # L55 from 55 -> 0 (55 - 55 = 0, no wrap)
        result = dial.turnDialFromString("L55")
        self.assertEqual(result, 0, "L55 from 55 should be 0")
        self.assertEqual(dial.currentTimesWePassedZero, 4, "Should not pass 0 (landing on 0 doesn't count)")
        self.assertEqual(dial.currentTimesWeStopAtZero, 2, "Should stop at 0 for the second time")
        
        # L1 from 0 -> 99 (0 - 1 = -1, wraps to 99)
        result = dial.turnDialFromString("L1")
        self.assertEqual(result, 99, "L1 from 0 should be 99")
        self.assertEqual(dial.currentTimesWePassedZero, 5, "Should pass 0 once when wrapping backward")
        self.assertEqual(dial.currentTimesWeStopAtZero, 2, "Stop at 0 count unchanged")
        
        # L99 from 99 -> 0 (99 - 99 = 0, no wrap)
        result = dial.turnDialFromString("L99")
        self.assertEqual(result, 0, "L99 from 99 should be 0")
        self.assertEqual(dial.currentTimesWePassedZero, 5, "Should not pass 0 (landing on 0 doesn't count)")
        self.assertEqual(dial.currentTimesWeStopAtZero, 3, "Should stop at 0 for the third time")
        
        # R14 from 0 -> 14 (0 + 14 = 14, no wrap)
        result = dial.turnDialFromString("R14")
        self.assertEqual(result, 14, "R14 from 0 should be 14")
        self.assertEqual(dial.currentTimesWePassedZero, 5, "Should not pass 0 when moving forward from 0")
        self.assertEqual(dial.currentTimesWeStopAtZero, 3, "Stop at 0 count unchanged")
        
        # L82 from 14 -> 32 (14 - 82 = -68, wraps to 32)
        result = dial.turnDialFromString("L82")
        self.assertEqual(result, 32, "L82 from 14 should be 32")
        self.assertEqual(dial.currentTimesWePassedZero, 6, "Should pass 0 once when wrapping backward")
        self.assertEqual(dial.currentTimesWeStopAtZero, 3, "Stop at 0 count unchanged")

        # assert the zero pass count
        self.assertEqual(dial.currentTimesWePassedZero, 6, "Total times passed zero should be 6")
        self.assertEqual(dial.currentTimesWeStopAtZero, 3, "Total times stopped at zero should be 3")

if __name__ == '__main__':
    unittest.main()
