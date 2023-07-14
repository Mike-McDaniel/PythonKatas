import unittest
from sequenceabstractions import addTenToAll, concatLetters, countLetters, duplicateLetters, firstLetters, firstNLast, mysteryMath, oddOrEven, oddOrPlus10, onlyOdds, reverseStrings, startsWithS, sumList

class TestSequenceAbstractions(unittest.TestCase):

	#                   mapping functions
    # a[N] -> b[N]
    # transforming a list = "mapping" a list
    # map = output list is always the same length as the input list

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


	#                   filter functions
    # must have an if statement
    # a[N] -> a[0-N]
    # return empty to N items, where N is the length of the list

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


    #                   reduce functions  
    # a[N] -> b
    # collapsing a list into a single thing
    # expanding a list into a many things

    def test_sum(self):
        self.assertEqual(sumList([1,1,1,2]), 5)

    def test_concatLetters(self):
        self.assertEqual(concatLetters([]), "")
        self.assertEqual(concatLetters(["S","a", "m"]), "Sam")

    def test_reverseStrings(self):
        self.assertEqual(reverseStrings([]), "")
        self.assertEqual(reverseStrings(["S","a", "m"]), "maS")

    def test_duplicateLetters(self):
        self.assertEqual(duplicateLetters([]), "")
        self.assertEqual(duplicateLetters(["a", "b", "c"]), "cbaabc")

#                   exercise
# could be any kind of function (map, filter, reduce).
# steve write test, mike build function
 
    def test_countLetters(self):
        self.assertEqual(countLetters([]), [])
        self.assertEqual(countLetters(["sam", "steve", "mike"]), [3, 5, 4])

    def test_mysteryMath(self):
        self.assertEqual(mysteryMath([]), [])
        self.assertEqual(mysteryMath([5, 10, 15, 20]), [1, 2, 3, 4])

    def test_firstNLast(self):
        self.assertEqual(firstNLast([]), [])
        self.assertEqual(firstNLast(["test", "this", "out", "now"]),
                                       ["tt", "ts", "ot", "nw"])

if __name__ == '__main__':
    unittest.main()