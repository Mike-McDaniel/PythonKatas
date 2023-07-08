import unittest

from helpers import add10, add, dif, dif_between_sum_of_squares1_2, get_value, greeting, square, sum_of_squares1, sum_of_squares2

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
        self.assertEqual(sum_of_squares1(2), 8)
        self.assertEqual(sum_of_squares1(1), 2)

    def test_sum_of_squares2(self):
        self.assertEqual(sum_of_squares2(3), 18)

    def test_dif(self):
        self.assertEqual(dif(18,18), 0)
        self.assertEqual(dif(1), 1)
        self.assertEqual(dif(), 0)
        self.assertEqual(dif(3,2), 1)

    def test_dif_between_sum_of_squares1_2(self):
        self.assertEqual(dif_between_sum_of_squares1_2(2,1), 6)

    # "4D" getValue -> 4
    # "TS" getValue -> 10
    # "KS" getValue -> 13 
    # "AS" getValue -> 14 
    def test_get_value(self):
        self.assertEqual(get_value("4D"), 4)
        self.assertEqual(get_value("TS"), 10)
        self.assertEqual(get_value("JS"), 11)
        self.assertEqual(get_value("QS"), 12)
        self.assertEqual(get_value("KS"), 13)
        self.assertEqual(get_value("AS"), 14) # imperfect (leaky) abstraction in blackjack. This is poker

    # "4D" get_suit -> "diamonds"
    # "TS" get_suit -> "spades"
    # "KH" get_suit -> "hearts"
    # "AC" get_suit -> "clubs"

if __name__ == '__main__':
    unittest.main()