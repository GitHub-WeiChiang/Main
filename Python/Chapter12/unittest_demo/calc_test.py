__author__ = "ChiangWei"
__date__ = "2022/5/30"

import unittest
import calc

class CalcTestCase(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.args = (3, 2)

    def tearDown(self):
        print("tearDown")
        self.args = None

    def test_plus(self):
        print("test_plus")
        expected = 5
        result = calc.plus(*self.args)
        self.assertEqual(expected, result)

    def test_minus(self):
        print("test_minus")
        expected = 1
        result = calc.minus(*self.args)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
