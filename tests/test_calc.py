import unittest
from src.calc import add, divide


class TestCalc(unittest.TestCase):

    def test_add(self):
        expectedResult = 15
        result = add(10, 5)
        self.assertEqual(expectedResult, result)

    def test_divide(self):
        # self.assertRaises(ValueError, divide, 10, 0)
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == '__main__':
    unittest.main()
