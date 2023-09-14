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

def detect_pair(hand):
    for face in count_faces(hand): 
        if count_faces(hand)[face] == 2:
            return True
    return False

# def detect_pair(hand):
#     face_counts = count_faces(hand)
#     for face in face_counts:
#         count = face_counts[face] 
#         if count == 2:
#             return True
#     return False

# def count_faces(hand):
#     face_counts = {}
#     for card in hand:
#         if (card["Face"] in face_counts):
#             face_counts[card["Face"]] = face_counts[card["Face"]] + 1 # Please explain: How is the empty dictionary populating?
#         else:
#             face_counts[card["Face"]] = 1
#     return face_counts

def count_faces(hand):
    face_counts = {}
    for card in hand:
        face = card["Face"]
        if (face in face_counts):
            face_counts[face] = face_counts[face] + 1
        else:
            face_counts[face] = 1
    return face_counts


def detect_3oak(hand):
    for face in count_faces(hand):
        if count_faces(hand)[face] == 3:
            return True
        return False   
    

def detect_4oak(hand):
    for face in count_faces(hand):
        if count_faces(hand)[face] == 4:
            return True
        return False
    
def detect_fh(hand):
    if detect_pair(hand) == True and detect_3oak(hand) == True:
        return True
    return False

def count_suits(Hand):
    Count = {}
    for Card in Hand:
        if (Card['Suit'] in Count):
            Count[Card['Suit']] = Count[Card['Suit']] +1
        else:
            Count[Card['Suit']] = 1
    return Count

def detect_flush(Hand):
    for Suit in count_suits(Hand):
        if count_suits(Hand)[Suit] == 5:
            return True
    return False

def detect_straight(Hand):
    Faces = []
    for Card in Hand:
        Faces.append(Card['Face'])
    Faces.sort()
    PreviousFace = Faces[0]
    for CurrentFace in Faces[1:]:
        if (PreviousFace + 1 == CurrentFace):
            PreviousFace = CurrentFace
        else:
            return False
    return True