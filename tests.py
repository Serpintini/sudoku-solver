from unittest import TestCase
from solve import *

class TestPuzzle(TestCase):
    def setUp(self):
        self.me = Solver()
        
    def test_box(self):
        self.assertEqual(self.me.puzzle[(1,3)].get_box(), 1)
        self.assertEqual(self.me.puzzle[(5,3)].get_box(), 2)
        self.assertEqual(self.me.puzzle[(1,9)].get_box(), 7)
        self.assertEqual(self.me.puzzle[(9,9)].get_box(), 9)

    def test_puzzle_easy(self):
        self.me.puzzle[(1, 1)].value = 5
        self.me.puzzle[(2, 1)].value = 8
        self.me.puzzle[(5, 1)].value = 6
        self.me.puzzle[(6, 1)].value = 7
        self.me.puzzle[(7, 1)].value = 2

        self.me.puzzle[(4, 2)].value = 9
        self.me.puzzle[(5, 2)].value = 8
        self.me.puzzle[(6, 2)].value = 2
        self.me.puzzle[(7, 2)].value = 5
        self.me.puzzle[(8, 2)].value = 7
        self.me.puzzle[(9, 2)].value = 1

        self.me.puzzle[(1, 3)].value = 2
        self.me.puzzle[(3, 3)].value = 1
        self.me.puzzle[(7, 3)].value = 9

        self.me.puzzle[(2, 4)].value = 9
        self.me.puzzle[(4, 4)].value = 2
        self.me.puzzle[(6, 4)].value = 4
        self.me.puzzle[(7, 4)].value = 7
        self.me.puzzle[(9, 4)].value = 8

        self.me.puzzle[(1, 5)].value = 7
        self.me.puzzle[(2, 5)].value = 3
        self.me.puzzle[(8, 5)].value = 2
        self.me.puzzle[(9, 5)].value = 5

        self.me.puzzle[(2, 6)].value = 1
        self.me.puzzle[(3, 6)].value = 2
        self.me.puzzle[(4, 6)].value = 8
        self.me.puzzle[(5, 6)].value = 7
        self.me.puzzle[(9, 6)].value = 9

        self.me.puzzle[(1, 7)].value = 1
        self.me.puzzle[(3, 7)].value = 7
        self.me.puzzle[(4, 7)].value = 5
        self.me.puzzle[(7, 7)].value = 8

        self.me.puzzle[(3, 8)].value = 6
        self.me.puzzle[(5, 8)].value = 2
        self.me.puzzle[(8, 8)].value = 4
        self.me.puzzle[(9, 8)].value = 7

        self.me.puzzle[(3, 9)].value = 3
        self.me.puzzle[(7, 9)].value = 9

        self.me.full_solve()


        










