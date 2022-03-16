import unittest
from Core.helper.date import monthname

class TestMontName(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(monthName(1), 'March')
        