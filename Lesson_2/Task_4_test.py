import unittest

from Task_4 import range_


class TestRange(unittest.TestCase):

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            range_()

    def test_one_positive_argument(self):
        self.assertEqual(range_(10), list(range(10)))

    def test_one_negative_argument(self):
        self.assertEqual(range_(-10), list(range(-10)))

    def test_one_zero_argument(self):
        self.assertEqual(range_(0), list(range(0)))

    def test_two_ascending_arguments(self):
        self.assertEqual(range_(10, 20), list(range(10, 20)))

    def test_two_descending_arguments(self):
        self.assertEqual(range_(20, 10), list(range(20, 10)))

    def test_two_ascending_arguments_with_positive_step(self):
        self.assertEqual(range_(10, 20, 2), list(range(10, 20, 2)))

    def test_two_ascending_arguments_with_negative_step(self):
        self.assertEqual(range_(10, 20, -2), list(range(10, 20, -2)))

    def test_two_descending_arguments_with_positive_step(self):
        self.assertEqual(range_(20, 10, 2), list(range(20, 10, 2)))

    def test_two_descending_arguments_with_negative_step(self):
        self.assertEqual(range_(20, 10, -2), list(range(20, 10, -2)))

    def test_zero_step(self):
        with self.assertRaises(ValueError):
            range_(10, 20, 0)


if __name__ == '__main__':
    unittest.main()
