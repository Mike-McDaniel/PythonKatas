import unittest

from PokerKataPractice import detect_pair, get_card, get_face, get_hand, get_suit, parse_hand, parse_hand_string

class TestPokerKataPractice(unittest.TestCase):


    
    def test_get_face(self):
        self.assertEqual(get_face("2X"), 2)
        self.assertEqual(get_face("KX"), 13)

    def test_get_suit(self):
        self.assertEqual(get_suit("XC"), "Clubs")
        self.assertEqual(get_suit("XD"), "Diamonds")

    def test_get_card(self):
        self.assertEqual(get_card("2S")["Face"], 2)
        self.assertEqual(get_card("2S")["Suit"], "Spades") # ?
    
    def test_get_hand(self):
        hand1 = get_hand(["JC", "4D"])
        card0 = hand1[0]
        self.assertEqual(card0["Face"], 11)
        card = get_hand(["JC", "4D"])
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

    def test_detect_pair_is_pair(self):
        hand = [
            {'Face': 6, 'Suit': 'Clubs'}, 
            {'Face': 4, 'Suit': 'Diamonds'}, 
            {'Face': 6, 'Suit': 'Diamonds'}, 
            {'Face': 5, 'Suit': 'Hearts'}, 
            {'Face': 3, 'Suit': 'Hearts'}]
        isPair = detect_pair(hand)
        self.assertEqual(isPair, True)

    def test_detect_pair_is_not_pair(self):
        hand = [
            {'Face': 6, 'Suit': 'Clubs'}, 
            {'Face': 4, 'Suit': 'Diamonds'}, 
            {'Face': 8, 'Suit': 'Diamonds'}, 
            {'Face': 5, 'Suit': 'Hearts'}, 
            {'Face': 3, 'Suit': 'Hearts'}]
        isPair = detect_pair(hand)
        self.assertEqual(isPair, False)
    
    

if __name__ == '__main__':
    unittest.main()