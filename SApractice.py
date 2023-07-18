def addTenToAll(numbers):
    new_numbers = []
    for number in numbers:
        new_numbers.append(number + 10)
    return new_numbers

def FirstLetters(names):
    letter = []
    for name in names:
        letter.append(name[0])
    return letter

def OddOrEven(numbers):
    strings = []
    for number in numbers:
        if number % 2 == 0:
            strings.append("even")
        else:
            strings.append("odd")
    return strings

def OddOrPlus10(numbers):
    new_elements = []
    for number in numbers:
        if number % 2 == 1:
            new_elements.append("odd")
        else:
            new_elements.append(number + 10)
    return new_elements

def lengthOfString(strings):
    lengths = []
    for string in strings:
        lengths.append(string + ": " + str(len(string)))
    return lengths