import unittest

from Experimentations import add, concatLetters, count_faces, count_suits, detect_3oak, detect_4oak, detect_fh, detect_flush, detect_pair, get_card, get_face, get_hand, get_suit, number_range1, number_range2, number_range_list, parse_hand, parse_hand_string

class TestExperimentations(unittest.TestCase):

    def test_number_range1(self):
        self.assertEqual(number_range1(0), range(0, 0))
        self.assertEqual(number_range1(1), range(0, 1))
        self.assertEqual(number_range1(2), range(0, 2))
        self.assertEqual(range(3), range(0, 3))
    
    def test_number_range2(self):
        self.assertEqual(number_range2(0), "")
        self.assertEqual(number_range2(1), "-")
        self.assertEqual(number_range2(2), "--")


    def test_number_range_list(self):
        self.assertListEqual(number_range_list([0]), [range(0, 0)])
        self.assertListEqual(number_range_list([1, 2, 3]), [range(0, 1), range(0, 2), range(0, 3)])

    def test_add(self):
        self.assertEqual(add([0]), 0)
        self.assertEqual(add([1, 2, 3]), 6)

    def test_concatLetters(self):
        self.assertEqual(concatLetters([]), "")
        self.assertEqual(concatLetters(["S","a", "m"]), "Sam")



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

    def test_get_suit(self):
        self.assertEqual(get_suit("6C"), "Clubs")
        self.assertEqual(get_suit("4D"), "Diamonds")
        self.assertEqual(get_suit("2H"), "Hearts")
        self.assertEqual(get_suit("QS"), "Spades")

    def test_get_card(self):
        card1 = get_card("6C")
        self.assertEqual(card1["suit"], "Clubs")
        self.assertEqual(card1["face"], 6)
        card2 = get_card("4D")
        self.assertEqual(card2["suit"], "Diamonds")
        self.assertEqual(card2["face"], 4)
        self.assertEqual(get_card("2H")["suit"], "Hearts")
        self.assertEqual(get_card("QS")["suit"], "Spades")

    def test_get_hand(self):
        hand = get_hand(["6C", "4D"])
        self.assertEqual(hand[0]["suit"], "Clubs")
        self.assertEqual(hand[0]["face"], 6)
        self.assertEqual(hand[1]["suit"], "Diamonds")
        self.assertEqual(hand[1]["face"], 4)

    def test_parse_hand_string(self):
        self.assertEqual(parse_hand_string("6C"), ["6C"])
        self.assertEqual(parse_hand_string("6C 4D"), ["6C", "4D"])

    def test_parse_hand(self):
        hand = parse_hand("6C 4D")
        self.assertEqual(hand[0]["suit"], "Clubs")
        self.assertEqual(hand[0]["face"], 6)
        self.assertEqual(hand[1]["suit"], "Diamonds")
        self.assertEqual(hand[1]["face"], 4)

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
        hand = [
            {'Face': 6, 'Suit': 'Clubs'},
            {'Face': 4, 'Suit': 'Diamonds'}, 
            {'Face': 6, 'Suit': 'Diamonds'}, 
            {'Face': 5, 'Suit': 'Hearts'}, 
            {'Face': 3, 'Suit': 'Hearts'}]
        count = count_faces(hand)
        self.assertEqual(count,  {6: 2, 4: 1, 5: 1, 3: 1})

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