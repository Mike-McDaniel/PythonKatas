def greeting(username): # github test 2
    return 'hello ' + username +'!'

def upper(x):
    return (x.upper())

def add(x=0,y=0,z=0):
    return x+y+z

def add10(x):
    return x+10

def square(x):
    return x**2

def sum_of_squares1(x):
    return add(square(x), square(x))

def sum_of_squares2(x):
    square_of_x=square(x)
    return add(square_of_x, square_of_x)

def dif(x=0,y=0):
    return x-y

def dif_between_sum_of_squares1_2(x,y):
    sum_1=sum_of_squares1(x)
    sum_2=sum_of_squares2(y)
    r = dif(sum_1,sum_2) # calling the dif function with (passing) the variables sum1,sum2 as the parameters
    return r


#  python imperative procedural language (executes line by line, stepping into functions with separate scope)
#  sql    declarative           language (executes all lines at the same time)

# call a function (with parameters)
# store the result in a variable
# returning the variable
# passing (going in)
# returning (coming out)

#  DEPENDENCY GRAPH or DEPENDENCY HEIRARCHY or DEPENDENCY TREE (when it is not running)
#  CALL STACK (when running)

#                test_dif_between_sum_of_squares1_2
#                                 |
#                  dif_between_sum_of_squares1_2
#                /               |                   \
#    sum_of_squares1        sum_of_squares2          dif
#    /          \             /          \
# square        add        square        add 

def get_value(card):

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

# ()  means calling a function.
# []  means indexing a dict/string/array/list.

def get_suit(card):

    card_dict_suit = {
        "C": "clubs",
        "D": "diamonds",
        "H": "hearts",
        "S": "spades",
    }
    second_letter = card[1]
    return card_dict_suit[second_letter]


def get_suit_value(card):
    card_dict_suit = {
        "C": 0.2,
        "D": 0.4,
        "H": 0.6,
        "S": 0.8,
    }
    second_letter = card[1]
    return card_dict_suit[second_letter]


def sum_of_card_value(card):
    card=get_value(card) + get_suit_value(card)
    return card


def pair(card1,card2):
    card1=get_value(card1)
    card2=get_value(card2)
    score=add(card1,card2)
    return "PAIR OF ", (card1), "'s!!", score, "POINTS!"


def of_a_kind(card1,card2,card3,card4,card5):
    card1=get_value(card1)
    card2=get_value(card2)
    card3=get_value(card3)
    card4=get_value(card4)
    card5=get_value(card5)
    if card1 == card2:
        return add(card1,card2)
    

def two_of_a_kind(card1,card2,card3,card4,card5):
    card1=get_value(card1)
    card2=get_value(card2)
    card3=get_value(card3)
    card4=get_value(card4)
    card5=get_value(card5)
    score=add(card1,card2)
    if card1 == card2:
        return "PAIR OF ", (card1), "'s!!", score, "POINTS!"
    

def three_of_a_kind(card1,card2,card3,card4,card5):
    card1=get_value(card1)
    card2=get_value(card2)
    card3=get_value(card3)
    card4=get_value(card4)
    card5=get_value(card5)
    score=add(card1,card2,card3)
    if card1 == card2 == card3:
        return "THREE ", (card1), "'s!!", score, "POINTS!"