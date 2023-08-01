def get_face(card):
    card_dictionary_face = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14
    }
    return card_dictionary_face[card[0]]

def get_suit(card):
    card_dictionary_suit = {
        "C": "Clubs",
        "D": "Diamonds",
        "H": "Hearts",
        "S": "Spades"
    }
    return card_dictionary_suit[card[1]]

def get_card(card):
    card_dictionary = {
        "Face": get_face(card),
        "Suit": get_suit(card)
    }
    return card_dictionary

def get_hand(cards):
    return list(map(lambda card: get_card(card), cards))

def parse_hand_string(cards_string):
    return cards_string.split(" ")

def parse_hand(hand):
    return get_hand(parse_hand_string(hand))

def detect_pair(x):
    print(x)
    return False