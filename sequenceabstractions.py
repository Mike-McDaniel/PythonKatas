


# transforming a list
# "mapping" a list
#       map = output list is always the same length as the input list
# def addTenToAll(numbers):
# 	newNumbers = []
# 	for x in numbers:
# 		newNumbers.append(x + 10)
# 	return newNumbers

def addTenToAll(numbers):
	new_numbers = []
	for x in numbers:
		new_numbers.append(x + 10)
	return new_numbers


# def firstLetters(names):
# 	newNames = []
# 	for name in names:
# 		newNames.append(name[0])
# 	return newNames

def firstLetters(names):
	new_names = []
	for letter in names:
		new_names.append(letter[0])
	return new_names

def oddOrEven(numbers):
	newNumbers = []
	for number in numbers:
		if (number % 2) == 0:
			newNumbers.append("even")
		else:
			newNumbers.append("odd")
	return newNumbers

def oddOrPlus10(numbers):
	newNumbers = []
	for number in numbers:
		if (number % 2) == 0:
			newNumbers.append(number + 10)
		else:
			newNumbers.append("odd")
	return newNumbers

# filter functions (must have if statement)
# return empty to N items, where N is the length of the list

def onlyOdds(numbers):
	newNumbers = []
	for number in numbers:
		if (number % 2) == 1:
			newNumbers.append(number)
	return newNumbers

def startsWithS(names):
	newNames = []
	for name in names:
		if name[0] == "S":
			newNames.append(name)
	return newNames