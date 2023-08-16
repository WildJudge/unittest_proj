import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], 0, "test"), 1)
        self.assertEqual(arrs.get([1, 2, 3], 2, "test"), 3)
        self.assertEqual(arrs.get([1, 2, 3], 5, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], -1, "test"), "test")
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], -5, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], 5), None)
        self.assertEqual(arrs.get([1, 2, 3], 0), 1)

    def test_my_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 0, 4), [1, 2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -2, -1), [3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -3, 4), [2, 3, 4])
        self.assertEqual(arrs.my_slice([], 0, 2), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, -1), [2, 3])
        self.assertEqual(arrs.my_slice([42], 0, 1), [42])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], start=-2, end=-4), [])
        self.assertEqual(arrs.my_slice([], end=2), [])


if __name__ == '__main__':
    unittest.main()
