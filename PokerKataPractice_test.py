import unittest

from PokerKataPractice import get_card, get_face, get_hand, get_suit, parse_hand, parse_hand_string

class TestPokerKataPractice(unittest.TestCase):


    
    def test_get_face(self):
        self.assertEqual(get_face("2X"), 2)
        self.assertEqual(get_face("KX"), 13)

    def test_get_suit(self):
        self.assertEqual(get_suit("XC"), "Clubs")
        self.assertEqual(get_suit("XD"), "Diamonds")

    def test_get_card(self):
        self.assertEqual(get_card("2S")["Face"], 2)
        self.assertEqual(get_card("2S")["Suit"], "Spades")
    
    def test_get_hand(self):
        card = get_hand(["JC", "4D"])
        self.assertEqual(get_hand(["JC", "4D"])[0]["Face"], 11)
        self.assertEqual(card[0]["Face"], 11)
        self.assertEqual(get_hand(["JC", "4D"])[1]["Suit"], "Diamonds")
        self.assertEqual(card[1]["Suit"], "Diamonds")
    
    def test_parse_hand_string(self):
        self.assertEqual(parse_hand_string("XX XX"), ["XX", "XX"])
        self.assertEqual(parse_hand_string("XX XX XX XX XX"), ["XX", "XX", "XX", "XX", "XX"])

    def test_parse_hand(self):
        hand = parse_hand("6C 4D")
        self.assertEqual(hand[0]["Suit"], "Clubs")
        self.assertEqual(hand[0]["Face"], 6)
        self.assertEqual(hand[1]["Suit"], "Diamonds")
        self.assertEqual(hand[1]["Face"], 4)
    
    

if __name__ == '__main__':
    unittest.main()