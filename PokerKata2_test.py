import unittest

from PokerKata2 import get_card, get_face, get_hand, get_suit, parse_hand, parse_hand_string

class TestPokerKata2(unittest.TestCase):


    # "4D" get_value -> 4
    # "TS" get_value -> 10
    # "KS" get_value -> 13 
    # "AS" get_value -> 14 
    
    def test_get_face(self):
        self.assertEqual(get_face("2H"), 2)
        self.assertEqual(get_face("3C"), 3)
        self.assertEqual(get_face("4D"), 4)
        self.assertEqual(get_face("5D"), 5)
        self.assertEqual(get_face("6C"), 6)
        self.assertEqual(get_face("7D"), 7)
        self.assertEqual(get_face("8S"), 8)
        self.assertEqual(get_face("9D"), 9)
        self.assertEqual(get_face("TS"), 10)
        self.assertEqual(get_face("JS"), 11)
        self.assertEqual(get_face("QS"), 12)
        self.assertEqual(get_face("KS"), 13)
        self.assertEqual(get_face("AS"), 14)
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

    def test_get_card(self):
        card1 = get_card("6C")
        self.assertEqual(card1["suit"], "clubs")
        self.assertEqual(card1["face"], 6)
        card2 = get_card("4D")
        self.assertEqual(card2["suit"], "diamonds")
        self.assertEqual(card2["face"], 4)
        self.assertEqual(get_card("2H")["suit"], "hearts")
        self.assertEqual(get_card("QS")["suit"], "spades")

    def test_get_hand(self):
        self.assertEqual(get_hand([]), [])
        hand = get_hand(["6C", "4D"])
        self.assertEqual(hand[0]["suit"], "clubs")
        self.assertEqual(hand[0]["face"], 6)
        self.assertEqual(hand[1]["suit"], "diamonds")
        self.assertEqual(hand[1]["face"], 4)

    def test_parse_hand_string(self):
        self.assertEqual(parse_hand_string("6C"), ["6C"])
        self.assertEqual(parse_hand_string("6C 4D"), ["6C", "4D"])

    def test_parse_hand(self):
        hand = parse_hand("6C 4D")
        self.assertEqual(hand[0]["suit"], "clubs")
        self.assertEqual(hand[0]["face"], 6)
        self.assertEqual(hand[1]["suit"], "diamonds")
        self.assertEqual(hand[1]["face"], 4)
    

if __name__ == '__main__':
    unittest.main()