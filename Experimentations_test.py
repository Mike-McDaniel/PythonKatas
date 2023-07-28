import unittest

from Experimentations import number_range1, number_range2, number_range_list

class TestExperimentations(unittest.TestCase):

    def test_number_range1(self):
        self.assertEqual(number_range1(0), range(0, 0))
        self.assertEqual(number_range1(1), range(0, 1))
        self.assertEqual(number_range1(2), range(0, 2))
        self.assertEqual(range(3), range(0, 3))
    
    def test_number_range2(self):
        self.assertEqual(number_range2(0), "")
        self.assertEqual(number_range2(1), "-")
        self.assertEqual(number_range2(2), "--")


    def test_number_range_list(self):
        self.assertListEqual(number_range_list([0]), [range(0, 0)])
        self.assertListEqual(number_range_list([1, 2, 3]), [range(0, 1), range(0, 2), range(0, 3)])


if __name__ == '__main__':
    unittest.main()