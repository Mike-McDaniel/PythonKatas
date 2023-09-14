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

def count_suits(Hand):
    Count = {}
    for Card in Hand:
        if (Card['Suit'] in Count):
            Count[Card['Suit']] = Count[Card['Suit']] +1
        else:
            Count[Card['Suit']] = 1
    # print(Count)
    return Count

def detect_flush1(Hand):
    for Suit in count_suits(Hand):
        if count_suits(Hand)[Suit] == 5:
            return True
    return False

def detect_flush(Hand):
    # memoization
    counts = count_suits(Hand)
    for Suit in counts:
        if counts[Suit] == 5:
            return True
    return False

# if sorted (small->large), each face is +1 from the previous face, starting with the smallest

# there exists 1 of each face, and the smallest and largest are 4 apart

# (tree-based solution) starting with a number, does there exist -1/+1 from that number in the list, keep walking until you've seen 5 numbers
def detect_straight(Hand):
    # extract faces
    Faces = []
    for Card in Hand:
        Faces.append(Card['Face'])
    # sort faces small to large
    Faces.sort()

    # ensure each face is +1 the previous face
    # previousFace = Faces.pop(0) 
    # for currentFace in Faces: 
    #     if(previousFace + 1 == currentFace):
    #         previousFace = currentFace
    #     else:
    #         return False
    # return True

    previousFace = Faces[0] 
    for currentFace in Faces[1:]:     #  Faces[1:] keeps everything from index 1 to the end of the list
        if(previousFace + 1 == currentFace):
            previousFace = currentFace
        else:
            return False

    return True