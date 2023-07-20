import unittest

from Dictionaries import getZipCodes

class TestDictionaries(unittest.TestCase):

    def test_CanGetTheZipCodes(self):
        stevesAddress = {
            "street": "49 Germantown",
            "city": "Germantown",
            "state": "PA",
            "zip": "138322",
        }
        samsAddress = {
            "street": "44 Germantown",
            "city": "Jose",
            "state": "CA",
            "zip": "914321"
        }
        self.assertEqual(getZipCodes([]), [])
        self.assertEqual(getZipCodes([stevesAddress, samsAddress]), [ "138322", "914321"])


if __name__ == '__main__':
    unittest.main()
