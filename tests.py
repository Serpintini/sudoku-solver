from unittest import TestCase
from solve import *

class TestPuzzle(TestCase):
    def setUp(self):
        self.me = Solver()
        
    def test_box(self):
        self.assertEqual(self.me.get_box(1, 3), 1)
        self.assertEqual(self.me.get_box(5, 3), 2)
        self.assertEqual(self.me.get_box(1, 9), 7)
        self.assertEqual(self.me.get_box(9, 9), 9)


