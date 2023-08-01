import unittest

from PokerKataPractice import get_face

class TestPokerKataPractice(unittest.TestCase):


    
    def test_get_face(self):
        self.assertEqual(get_face("2H"), 2)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def test_get_suit(self):
    #     self.assertEqual(get_suit("6C"), "clubs")
    #     self.assertEqual(get_suit("4D"), "diamonds")
    #     self.assertEqual(get_suit("2H"), "hearts")
    #     self.assertEqual(get_suit("QS"), "spades")

    # def test_get_card(self):
    #     card1 = get_card("6C")
    #     self.assertEqual(card1["suit"], "clubs")
    #     self.assertEqual(card1["face"], 6)
    #     card2 = get_card("4D")
    #     self.assertEqual(card2["suit"], "diamonds")
    #     self.assertEqual(card2["face"], 4)
    #     self.assertEqual(get_card("2H")["suit"], "hearts")
    #     self.assertEqual(get_card("QS")["suit"], "spades")

    # def test_get_hand(self):
    #     self.assertEqual(get_hand([]), [])
    #     hand = get_hand(["6C", "4D"])
    #     self.assertEqual(hand[0]["suit"], "clubs")
    #     self.assertEqual(hand[0]["face"], 6)
    #     self.assertEqual(hand[1]["suit"], "diamonds")
    #     self.assertEqual(hand[1]["face"], 4)

    # def test_parse_hand_string(self):
    #     self.assertEqual(parse_hand_string("6C"), ["6C"])
    #     self.assertEqual(parse_hand_string("6C 4D"), ["6C", "4D"])

    # def test_parse_hand(self):
    #     hand = parse_hand("6C 4D")
    #     self.assertEqual(hand[0]["suit"], "clubs")
    #     self.assertEqual(hand[0]["face"], 6)
    #     self.assertEqual(hand[1]["suit"], "diamonds")
    #     self.assertEqual(hand[1]["face"], 4)
    

if __name__ == '__main__':
    unittest.main()