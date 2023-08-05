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