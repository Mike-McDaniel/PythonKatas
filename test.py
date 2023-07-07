import unittest

from helpers import add10, add, dif_between_sumofsquares1_2, greeting, square, sum_of_squares1, sum_of_squares2

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_string_stuff(self):
        self.assertEqual('5' +'6', '56')
        self.assertEqual(5 + 6, 11)
        self.assertEqual('5+6', '5+6')

    def test_hello(self):
        self.assertEqual(greeting('steve'), 'hello steve!')
        self.assertEqual(greeting('dave'), 'hello dave!')

    def test_add(self):
        self.assertEqual(add(1,2,3), 6)
        self.assertEqual(add(4,5,1), 10)
        self.assertEqual(add(1,1), 2)
        self.assertEqual(add(1), 1)
        self.assertEqual(add(), 0)

    def test_add10(self):
        self.assertEqual(add10(5), 15)

    def test_square(self):
        self.assertEqual(square(5), 25)

    def test_sum_of_squares1(self):
        self.assertEqual(sum_of_squares1(3), 18)

    def test_sum_of_squares2(self):
        self.assertEqual(sum_of_squares2(3), 18)

    def test_dif_between_sumofsquares1_2(self):
        self.assertEqual(dif_between_sumofsquares1_2(18,18), 0)
        self.assertEqual(dif_between_sumofsquares1_2(1), 1)
        self.assertEqual(dif_between_sumofsquares1_2(), 0)
        

if __name__ == '__main__':
    unittest.main()