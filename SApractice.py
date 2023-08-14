# Mapping

def addTen(number):
    return number + 10


# addTen = (lambda number: number + 10)

def addTenToAll(numbers):
    return list(map(lambda number: number + 10, numbers))

# def XaddTenToAll(numbers):
#     new_numbers = []
#     for number in numbers:
#         new_numbers.append(number + 10)
#     return new_numbers

def FirstLetters(names):
    return list(map(lambda name: name[0], names))

# def XFirstLetters(names):
#     letter = []
#     for name in names:
#         letter.append(name[0])
#     return letter

# helper function
def IsEven(number):
    return number % 2 == 0

def NumberToOddOrEven(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
    
def NumberToOddOrEven(number):
    if IsEven(number):
        return "even"
    else:
        return "odd"
    
# helper function
def NumberToOddOrEven(number):
    return "even" if number % 2 == 0 else "odd"

# orchestrator function    
def NumberToOddOrEven(number):
    return "even" if IsEven(number) else "odd"


# orchestrator function
def OddOrEven(numbers):
    return list(map(NumberToOddOrEven, numbers))

def OddOrEven(numbers):
    O_or_E = []
    for number in numbers:
        if number % 2 == 1:
            O_or_E.append("odd")
        else:
            O_or_E.append("even")
    return O_or_E

def OddOrPlus10(numbers):
    new_elements = []
    for number in numbers:
        if number % 2 == 1:
            new_elements.append("odd")
        else:
            new_elements.append(number + 10)
    return new_elements

def HOddOrPlus10(number):
    return "odd" if number % 2 == 1 else (number + 10)

def OddOrPlus10(numbers):
    return list(map(HOddOrPlus10, numbers))

def lengthOfString(strings):
    return list(map(lambda string: string + ": " + str(len(string)), strings))

def XlengthOfString(strings):
    lengths = []
    for string in strings:
        lengths.append(string + ": " + str(len(string)))
    return lengths



# Filter
def OnlyOdds(numbers):
    return list(filter(lambda number: number % 2 == 1, numbers))

def XOnlyOdds(numbers):
    odds = []
    for number in numbers:
        if number % 2 == 1:
            odds.append(number)
    return odds

def StartsWithS(names):
    return list(filter(lambda name: name[0] == "S", names))

def XStartsWithS(names):
    s_names = []
    for name in names:
        if name[0] == "S":
            s_names.append(name)
    return s_names

def onlyevenstrings(strings):
    return list(filter(lambda string: len(string) % 2 == 0, strings))

def onlyevenstrings(strings):
    return list(filter(lambda string: IsEven(len(string)), strings))

def onlyevenstrings(strings):
    e_strings = []
    for string in strings:
        if len(string) % 2 == 0:
            e_strings.append(string)
    return e_strings



# Reduce

def sumList(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

def concatLetters(letters):
    name = ""
    for letter in letters:
        name = name + letter
    return name

def reverseStrings(letters):
    r_name = ""
    for letter in letters:
        r_name = letter + r_name
    return r_name

def duplicateLetters(letters):
    dup_string = ""
    for letter in letters:
        dup_string = letter + dup_string + letter
    return dup_string



# Exercise 1

def XcountLetters(strings):
    counts = []
    for string in strings:
        counts.append(len(string))
    return counts

def countLetters(strings):
    return list(map(lambda string: len(string), strings))

def XmysteryMath(numbers):
    new_numbers = []
    for number in numbers:
        new_numbers.append(number / 5)
    return new_numbers

def mysteryMath(numbers):
    return list(map(lambda number: number / 5, numbers))

def XfirstNLast(strings):
    fNl = []
    for string in strings:
        fNl.append(string[0] + string[len(string)-1])
    return fNl

def firstNLast(strings):
    return list(map(lambda string: string[0] + string[len(string)-1], strings))



# Exercise 2

def Xsquare_of_name_length(names):
    lengths = []
    for name in names:
        lengths.append(len(name)**2)
    return lengths

def square_of_name_length(names):
    return list(map(lambda name: len(name)**2, names))

def Xsquare_of_single_name_length(name):
    length = len(name)
    return length**2

def square_of_single_name_length(name):
    return len(name)**2


# compound sequence abstractions
def XupperFirstLast(names):
    bigNamE = []
    for name in names:
        bigNamE.append(name[0].upper() + name[1:len(name)-1] + name[len(name)-1].upper())
    return bigNamE

def upperFirstLast(names):
    return list(map(lambda name: name[0].upper() + name[1:len(name)-1] + name[len(name)-1].upper(), names))

def XonlyBigEnough(names):
    bigNamE = []
    for name in names:
        if len(name) > 3:
            bigNamE.append(name)
    return bigNamE

def onlyBigEnough(names):
    return list(filter(lambda name: len(name) > 3, names))

def XbigEnoughNamesN(names):
    bigNamE = []
    for name in names:
        if len(name) > 3:
            name = name[0].upper() + name[1:len(name)-1] + name[len(name)-1].upper()
            bigNamE.append(name)
    return bigNamE

def bigEnoughNames(names):
    return onlyBigEnough(upperFirstLast(names))

