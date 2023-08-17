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