import unittest

from helpers import add10, adder, greeting, square

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

    def test_adder(self):
        self.assertEqual(adder(1,2,3), 6)
        self.assertEqual(adder(4,5,1), 10)

    def test_add10(self):
        self.assertEqual(add10(5), 15)

    def test_square(self):
        self.assertEqual(square(5), 25)

if __name__ == '__main__':
    unittest.main()