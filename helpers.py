def greeting(username): # github test 2
    return 'hello ' +         username +'!'

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

    carddict = {
        "4": 4,
        "T": 10,
    }
    first_letter = card[0]
    return carddict[first_letter]

# ()  means calling a function
# []  means indexing a dict/string/array/list 