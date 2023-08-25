from functools import reduce


def number_range1(number):
    range(number)
    return range(number)

def number_range1(number):
    num_range = range(number)
    return num_range

def number_range2(number):
    num_range = ""
    for x in range(number):
        num_range = num_range + "-"
    return num_range


def number_range_list(numbers):
    num_range = []
    for number in numbers:
        num_range.append(range(number))
    return num_range


def add(numbers):
    sum = (0)
    for number in numbers:
        sum = sum + number
    print(sum)    
    return sum

def concatLetters(letters):
    word = ""
    for letter in letters:
        word = word + letter
    return word

def concatLetters(letters):
    return reduce((lambda word, letter: word + letter), letters, "")

# reduce((lambda x, y: x + y), li, 0) x is the accumulate (acc) similiar to a seed.
#                                     li is the list
#                                      0 is the seed

print(reduce((lambda sum, number: sum + number), [1,2,3,4,5]))

# Loop 1 
# sum = 1
# number = 2 
# return 3

# Loop 2 
# sum = 3
# number = 3 
# return 6

# Loop 3 
# sum = 6
# number = 4 
# return = 10

# Loop 4 
# sum = 10
# number = 5
# return = 15

# 15


print(reduce((lambda sum, number: sum + number), [1,2,3,4,5], 0))

# Loop 1 
# sum = 0
# number = 1 
# return 1

# Loop 2 
# sum = 1
# number = 2  
# return 3

# ....

# Loop 5 
# sum = 10
# number = 5
# return = 15

# 15



def get_face(Card):
    Face = {
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        'T' : 10,
        'J' : 11,
        'Q' : 12,
        'K' : 13,
        'A' : 14
    }
    Value = Card[0]
    return Face[Value]

def get_suit(Card):
    Suit = {
        'D' : 'Diamonds',
        'C' : 'Clubs',
        'H' : 'Hearts',
        'S' : 'Spades'
    }
    Value = Card[1]
    return Suit[Value]

def get_card(Card):
    Card_call = {
        'face' : get_face(Card),
        'suit' : get_suit(Card)
    }
    return Card_call

def get_hand(Cards):
    Hand = []
    for Card in Cards:
        Hand.append(get_card(Card))
    return Hand

def parse_hand_string(Cards):
    return Cards.split(' ')

def parse_hand(Cards):
    return get_hand(parse_hand_string(Cards))

def count_faces(Hand):
    Count = {}
    for Card in Hand:
        if (Card['Face'] in Count):
            Count[Card['Face']] = Count[Card['Face']] +1
        else:
            Count[Card['Face']] = 1
    return Count

def detect_pair(Hand):
    for Face in count_faces(Hand):
        if count_faces(Hand)[Face] == 2:
            return True
    return False
        
def detect_3oak(Hand):
    for Face in count_faces(Hand):
        if count_faces(Hand)[Face] == 3:
            return True
    return False
        
def detect_4oak(Hand):
    for Face in count_faces(Hand):
        if count_faces(Hand)[Face] == 4:
            return True
    return False
        
def detect_fh(Hand):
    if detect_pair(Hand) == True and detect_3oak(Hand) == True:
        return True
    return False