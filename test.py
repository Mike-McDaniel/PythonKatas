import unittest

from helpers import greeting

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

if __name__ == '__main__':
    unittest.main()