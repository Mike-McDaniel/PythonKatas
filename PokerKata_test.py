import unittest

from PokerKata import add10, add, dif, dif_between_sum_of_squares1_2, finding_of_a_kind, get_suit, get_suit_value, get_value, greeting, of_a_kind, three_of_a_kind, two_of_a_kind, pair, square, sum_of_card_value, sum_of_squares1, sum_of_squares2, upper

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(upper('foo'), 'FOO')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO') # what's happening here?

    def test_string_stuff(self):
        self.assertEqual('5' +'6', '56')
        self.assertEqual(5 + 6, 11)
        self.assertEqual('5+6', '5+6') # what's happening here? Not importing a test but still passing?

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

    # "4D" get_value -> 4
    # "TS" get_value -> 10
    # "KS" get_value -> 13 
    # "AS" get_value -> 14 
    
    def test_get_value(self):
        self.assertEqual(get_value("2H"), 2)
        self.assertEqual(get_value("3C"), 3)
        self.assertEqual(get_value("4D"), 4)
        self.assertEqual(get_value("5D"), 5)
        self.assertEqual(get_value("6C"), 6)
        self.assertEqual(get_value("7D"), 7)
        self.assertEqual(get_value("8S"), 8)
        self.assertEqual(get_value("9D"), 9)
        self.assertEqual(get_value("TS"), 10)
        self.assertEqual(get_value("JS"), 11)
        self.assertEqual(get_value("QS"), 12)
        self.assertEqual(get_value("KS"), 13)
        self.assertEqual(get_value("AS"), 14)
                                        # ^^ this could be called imperfect (leaky) abstraction in blackjack,
                                        # because it can have more than one value.
                                        # This is poker and is not an issue. One value is ok.

    # "4D" get_suit -> "diamonds"
    # "TS" get_suit -> "spades"
    # "KH" get_suit -> "hearts"
    # "AC" get_suit -> "clubs"

    def test_get_suit(self):
        self.assertEqual(get_suit("6C"), "clubs")
        self.assertEqual(get_suit("4D"), "diamonds")
        self.assertEqual(get_suit("2H"), "hearts")
        self.assertEqual(get_suit("QS"), "spades")

    def test_get_suit_value(self):
        self.assertEqual(get_suit_value("6C"), 0.2)
        self.assertEqual(get_suit_value("4D"), 0.4)
        self.assertEqual(get_suit_value("2H"), 0.6)
        self.assertEqual(get_suit_value("QS"), 0.8)


    def test_sum_of_card_value(self):
        self.assertEqual(sum_of_card_value("2C"), 2.2)
        self.assertEqual(sum_of_card_value("4D"), 4.4)
        self.assertEqual(sum_of_card_value("AS"), 14.8)


    def test_pair(self):
        self.assertEqual(pair("4D", "4H"), ("PAIR OF ", 4, "'s!!", 8, "POINTS!"))
        self.assertEqual(pair("TS", "TC"), ("PAIR OF ", 10, "'s!!", 20, "POINTS!"))


    def test_of_a_kind(self):
        self.assertEqual(of_a_kind("4C", "4D", "2H", "3S", "6C"), 8)


    def test_two_of_a_kind(self):
        self.assertEqual(two_of_a_kind("4C", "4D", "2H", "3S", "6C"), 
                         ("PAIR OF ", 4, "'s!!", 8, "POINTS!"))
        

    def test_three_of_a_kind(self):
        self.assertEqual(three_of_a_kind("4C", "4D", "4H", "3S", "6C"), 
                         ("THREE ", 4, "'s!!", 12, "POINTS!"))
        self.assertEqual(three_of_a_kind("TC", "TD", "TH", "3S", "6C"), 
                         ("THREE ", 10, "'s!!", 30, "POINTS!"))
        
# combine of_a_kind functions next and improve on the logic.
# think about what happens when of_a_kind is not found.

    def test_finding_of_a_kind(self):
        self.assertEqual(finding_of_a_kind(["4C", "4D", "4H", "3S", "6C"]), {'4': 3, '3': 1, '6': 1})



if __name__ == '__main__':
    unittest.main()