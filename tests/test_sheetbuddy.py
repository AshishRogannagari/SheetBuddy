import unittest
from src.sheetbuddy import SheetBuddy

class TestSheetBuddy(unittest.TestCase):
    def test_read_csv(self):
        sb = SheetBuddy('https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv')
        self.assertIsNotNone(sb.data)
        self.assertEqual(sb.data.shape, (12, 4))

    def test_get_shape(self):
        sb = SheetBuddy('https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv')
        self.assertEqual(sb.get_shape(), (12, 4))

if __name__ == '__main__':
    unittest.main()
    