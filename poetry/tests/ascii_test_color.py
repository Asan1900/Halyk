import unittest
import sys
from color import colorize_string, generate_ascii_art
from io import StringIO



class TestColorizeString(unittest.TestCase):
    def test_colorize_string(self):
        self.assertEqual(colorize_string('Hello', 'red'),'\033[91mH\033[0m\033[91me\033[0m\033[91ml\033[0m\033[91ml\033[0m\033[91mo\033[0m')
        self.assertEqual(colorize_string('Hello', 'blue'), '\033[94mH\033[0m\033[94me\033[0m\033[94ml\033[0m\033[94ml\033[0m\033[94mo\033[0m')
        self.assertEqual(colorize_string('Hello', 'green'), '\033[92mH\033[0m\033[92me\033[0m\033[92ml\033[0m\033[92ml\033[0m\033[92mo\033[0m')

class TestGenerateAsciiArt(unittest.TestCase):
    def test_generate_ascii_art(self):
        captured_output - StringIO()
        sys.stdout = captured_output

        captured_output = StringIO()
        sys.stdout = captured_output

        generate_ascii_art('Hello', 'red', '1')
        self.assertEqual(captured_output.getvalue(), '\033[91mHel\033[0m\033[91mlo\033[0m\n')

        generate_ascii_art('Hello', 'blue', 'e')
        self.assertEqual(captured_output.getvalue(), '\033[94mH\033[0m\033[94m\033[94mel\033[0m\033[94ml\033[0m\033[94mo\033[0m\n')

        sys.stdout = sys.__stdout__



if __name__ == '__main__':
    unittest.main()

