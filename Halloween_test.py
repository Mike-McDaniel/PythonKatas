import unittest

from Halloween import is_spooky

class TeastHalloween(unittest.TestCase):

    def test_is_spooky(self):
        self.assertEqual(is_spooky(3), "Spooky")

    def test_is_not_spooky(self):
        self.assertEqual(is_spooky(2), "Safe")
    
    # def test_too_spooky(self):
    #     self.assertEqual(is_spooky(5), "Too Spooky")





if __name__ == '__main__':
    unittest.main()