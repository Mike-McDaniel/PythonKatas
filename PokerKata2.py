
# (string) => facestring
def get_face(card):
    card_dict_value = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    first_letter = card[0]
    return card_dict_value[first_letter]

# (string) => suitstring
def get_suit(card):
    card_dict_suit = {
        "C": "clubs",
        "D": "diamonds",
        "H": "hearts",
        "S": "spades",
    }
    second_letter = card[1]
    return card_dict_suit[second_letter]

# (string) => Card
def get_card(cardInput):
    card = {
        "face": get_face(cardInput),
        "suit": get_suit(cardInput)
        }
    return card

#        test_detector_pair
#               |
#          detect_pair
#                                                
#                                                
#                                                
#                                                
#               parse_hand   
#             /           \                            
#     parse_hand_string   get_hand                  
#                            |
#                         get_card             
#                        /        \ 
#                   get_suit      get_face      


# (string) => list<string> => list<Card>
                        # (string) => Card
                        # (string) => suitString
                        # (string) => faceString



# (list<string>) => list<Card>
def get_hand(cards):
    return list(map(lambda card: get_card(card), cards))


# (string) => list<string>
def parse_hand_string(cards_string):
    
    

# (string) => list<Card>
def parse_hand(cards_string):
    return get_hand(parse_hand_string(cards_string))