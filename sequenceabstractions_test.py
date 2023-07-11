import unittest
from sequenceabstractions import addTenToAll, firstLetters, oddOrEven, oddOrPlus10, onlyOdds, startsWithS

class TestSequenceAbstractions(unittest.TestCase):

	# mapping functions
    def test_addTenToAll(self):
		# arrange
        numbers = [1,2,3,4,5]
		# act
        actual = addTenToAll(numbers)
		# assert
        self.assertListEqual(actual, [11, 12, 13, 14, 15])

    def test_addFirstLetters(self):
		# arrange
        names = ["Steve", "Mike"]
		# act
        actual = firstLetters(names)
		# assert
        self.assertListEqual(actual, ["S", "M"])

    def test_OddOrEven(self):
		# arrange
        numbers = [1,2,2,2,1]
		# act
        actual = oddOrEven(numbers)
		# assert
        self.assertListEqual(actual, ["odd", "even",  "even",  "even", "odd" ])

    def test_OddOrPlus10(self):
		# arrange
        numbers = [1,2,4,6,1]
		# act
        actual = oddOrPlus10(numbers)
		# assert
        self.assertListEqual(actual, ["odd", 12, 14, 16, "odd" ])


	# filter functions
    def test_OnlyOdds(self):
		# arrange
        numbers = [1,2,4,6,7]
		# act
        actual = onlyOdds(numbers)
		# assert
        self.assertListEqual(actual, [1, 7])

    def test_OnlyOdds2(self):
		# arrange
        numbers = [2,4,6]
		# act
        actual = onlyOdds(numbers)
		# assert
        self.assertListEqual(actual, [])

    def test_StartsWithS(self):
		# arrange
        names = ["Steve", "Mike", "Sam"]
		# act
        actual = startsWithS(names)
		# assert
        self.assertListEqual(actual, ["Steve", "Sam"])


if __name__ == '__main__':
    unittest.main()