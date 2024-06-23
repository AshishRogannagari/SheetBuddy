import sys
import os
import unittest

# Ensure the src directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from sheetbuddy import SheetBuddy

class TestSheetBuddy(unittest.TestCase):
    def test_read_csv(self):
        sb = SheetBuddy('https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv')
        self.assertIsNotNone(sb.data)
        self.assertEqual(sb.data.shape, (12, 4))

    def test_get_shape(self):
        sb = SheetBuddy('https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv')
        self.assertEqual(sb.get_shape(), (12, 4))

    def test_get_column_info(self):
        sb = SheetBuddy('https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv')
        column_info = sb.get_column_info()
        self.assertIn('Column', column_info.columns)
        self.assertIn('Data Type', column_info.columns)
        self.assertIn('Description', column_info.columns)
        self.assertIn('Categorical/Numerical', column_info.columns)

if __name__ == '__main__':
    unittest.main()
