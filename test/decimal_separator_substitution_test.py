import unittest

from src.my_utilities import decimal_separator_substitution


class Test_TestDecimalSeparatorSubstitution(unittest.TestCase):
    def test_decimal_separator_substitution(self):
        self.assertEqual(decimal_separator_substitution('39,45'), '39.45')

    # This will fail
    def test_decimal_separator_substitution_surefail(self):
        self.assertEqual(decimal_separator_substitution('39.45'), '39,44')

if __name__ == '__main__':
    unittest.main()
