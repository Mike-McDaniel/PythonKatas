import unittest

from PokerKataPractice import count_faces, count_suits, detect_3oak, detect_4oak, detect_fh, detect_flush, detect_pair, get_card, get_face, get_hand, get_suit, parse_hand, parse_hand_string

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
            {'Face': 2, 'Suit': 'Diamonds'}, 
            {'Face': 5, 'Suit': 'Hearts'}, 
            {'Face': 6, 'Suit': 'Hearts'}]
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

    def test_count_faces_no_dups(self):
        hand = [
            {'Face': 6, 'Suit': 'Clubs'}, 
            {'Face': 4, 'Suit': 'Diamonds'}, 
            {'Face': 8, 'Suit': 'Diamonds'}, 
            {'Face': 5, 'Suit': 'Hearts'}, 
            {'Face': 3, 'Suit': 'Hearts'}]
        count = count_faces(hand)
        self.assertEqual(count[6], 1)
        self.assertEqual(count[4], 1)
        self.assertEqual(count[8], 1)
        self.assertEqual(count[5], 1)
        self.assertEqual(count[3], 1)

    def test_count_faces_dups(self):
        hand = [    # List of dictionaries.
            {'Face': 6, 'Suit': 'Clubs'}, # dictionary with multiple keys and values.
            {'Face': 4, 'Suit': 'Diamonds'}, 
            {'Face': 6, 'Suit': 'Diamonds'}, 
            {'Face': 5, 'Suit': 'Hearts'}, 
            {'Face': 3, 'Suit': 'Hearts'}]
        count = count_faces(hand)
        self.assertEqual(count,  {6: 2, 4: 1, 5: 1, 3: 1})
    

    def test_detect_3oak_is_3oak(self):
        hand = [
            {'Face': 6, 'Suit': 'Clubs'}, 
            {'Face': 4, 'Suit': 'Diamonds'}, 
            {'Face': 6, 'Suit': 'Diamonds'}, 
            {'Face': 5, 'Suit': 'Hearts'}, 
            {'Face': 6, 'Suit': 'Hearts'}]
        is3oak = detect_3oak(hand)
        self.assertEqual(is3oak, True)


    def test_detect_3oak_is_not_3oak(self):
        hand = [
            {'Face': 6, 'Suit': 'Clubs'}, 
            {'Face': 4, 'Suit': 'Diamonds'}, 
            {'Face': 2, 'Suit': 'Diamonds'}, 
            {'Face': 5, 'Suit': 'Hearts'}, 
            {'Face': 6, 'Suit': 'Hearts'}]
        is3oak = detect_3oak(hand)
        self.assertEqual(is3oak, False)   

    def test_detect_4oak_is_3oak(self):
        hand = [
            {'Face': 6, 'Suit': 'Clubs'}, 
            {'Face': 4, 'Suit': 'Diamonds'}, 
            {'Face': 6, 'Suit': 'Diamonds'}, 
            {'Face': 6, 'Suit': 'Aces'}, 
            {'Face': 6, 'Suit': 'Hearts'}]
        is3oak = detect_4oak(hand)
        self.assertEqual(is3oak, True)


    def test_detect_4oak_is_not_3oak(self):
        hand = [
            {'Face': 6, 'Suit': 'Clubs'}, 
            {'Face': 4, 'Suit': 'Diamonds'}, 
            {'Face': 2, 'Suit': 'Diamonds'}, 
            {'Face': 5, 'Suit': 'Hearts'}, 
            {'Face': 6, 'Suit': 'Hearts'}]
        is3oak = detect_4oak(hand)
        self.assertEqual(is3oak, False)

    def test_detect_fullhouse_is_fullhouse(self):
        hand = [
            {'Face': 6, 'Suit': 'Clubs'}, 
            {'Face': 4, 'Suit': 'Diamonds'}, 
            {'Face': 6, 'Suit': 'Diamonds'}, 
            {'Face': 4, 'Suit': 'Hearts'}, 
            {'Face': 6, 'Suit': 'Hearts'}]
        isfh = detect_fh(hand)
        self.assertEqual(isfh, True)

    def test_detect_fullhouse_is_not_fullhouse(self):
        hand = [
            {'Face': 6, 'Suit': 'Clubs'}, 
            {'Face': 4, 'Suit': 'Diamonds'}, 
            {'Face': 2, 'Suit': 'Diamonds'}, 
            {'Face': 5, 'Suit': 'Hearts'}, 
            {'Face': 6, 'Suit': 'Hearts'}]
        isfh = detect_fh(hand)
        self.assertEqual(isfh, False)

    def test_count_suits(self):
        hand = [
            {'Face': 6, 'Suit': 'Clubs'},
            {'Face': 4, 'Suit': 'Diamonds'}, 
            {'Face': 6, 'Suit': 'Diamonds'}, 
            {'Face': 5, 'Suit': 'Hearts'}, 
            {'Face': 3, 'Suit': 'Hearts'}]
        count = count_suits(hand)
        self.assertEqual(count,  {'Clubs': 1, 'Diamonds': 2, 'Hearts': 2})

    def test_detect_flush_is_flush(self):
        hand = [
            {'Face': 6, 'Suit': 'Hearts'}, 
            {'Face': 7, 'Suit': 'Hearts'}, 
            {'Face': 8, 'Suit': 'Hearts'}, 
            {'Face': 9, 'Suit': 'Hearts'}, 
            {'Face': 10, 'Suit': 'Hearts'}]
        isflush = detect_flush(hand)
        self.assertEqual(isflush, True)    

    def test_detect_flush_is_not_flush(self):
        hand = [
            {'Face': 6, 'Suit': 'Clubs'}, 
            {'Face': 4, 'Suit': 'Diamonds'}, 
            {'Face': 2, 'Suit': 'Diamonds'}, 
            {'Face': 5, 'Suit': 'Hearts'}, 
            {'Face': 6, 'Suit': 'Hearts'}]
        isflush = detect_flush(hand)
        self.assertEqual(isflush, False)





if __name__ == '__main__':
    unittest.main()