


# 					mapping functions
# a[N] -> b[N]
# transforming a list = "mapping" a list
# map = output list is always the same length as the input list

def addTenToAll(numbers):
	new_numbers = [] 				# seed
	for x in numbers:				# loop
		new_numbers.append(x + 10)	# condition
	return new_numbers				# return the accumulate

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


# 					filter functions
# must have an if statement (conditional and combination logic)
# a[N] -> a[0-N]
# return empty to N items, where N is the length of the list

def onlyOdds(numbers):
	newNumbers = [] 				  # seed
	for number in numbers: 			  # loop
		if (number % 2) == 1: 		  # conditional
			newNumbers.append(number) # combination logic
	return newNumbers 				  # return the accumlate

def startsWithS(names):
	newNames = []
	for name in names:
		if name[0] == "S":
			newNames.append(name)
	return newNames


# 					reduce functions
# a[N] -> b
# collapsing a list into a single thing
# expanding a list into a many things

def sumList(numbers):
	total = 0 				   # seed
	for number in numbers: 	   # loop
		total = total + number #condition
		# 0 + 1 -> 1
		# 1 + 1 -> 2
		# 2 + 1 -> 3
		# 3 + 2 -> 5
	return total 			   # return the accumulate

def concatLetters(letters):
	name = ""
	for letter in letters:
		name = name + letter # adding to the right of the seed
			   				 # position matters (positional)
	return name

def reverseStrings(letters):
	name = ""
	for letter in letters:
		name = letter + name # adding to the left of the seed
			   				 # position matters (positional)
	return name

def duplicateLetters(letters):
	dupstring = ""
	for letter in letters:
		dupstring = letter + dupstring + letter # (positional)
					# "a"  +    ""     +   "a"  ->   "aa"
					# "b"  +   "aa"    +   "b"  -> 	"baab"
					# "c"  +  "baab"   +   "c"  -> "cbaabc"
	return dupstring # return accumulate = "cbaabc"


#                   exercise
# could be any kind of function (map, filter, reduce).
# steve write test, mike build function

# how to start a function before building the loop and condition
# 			\/\/\/
# def functionname(perameter): 
	# seed = []
	# return seed

def countLetters(names): # (mapping)
	counts = []       			 # seed
	for name in names: 			 # loop
		counts.append(len(name)) # condition
	return counts     			 # return accumulate

def mysteryMath(numbers): # (mapping)
	mm = []
	for number in numbers:
		mm.append(number / 5)
	return mm

def firstNLast(names): # (mapping)
	fNL = []
	for name in names:
		fNL.append(name[0] + name[len(name)-1])
	return fNL

def square_of_name_length(name): # (mapping)
    counts = []
    for letter in name:
        counts.append(len(letter)**2)
    return counts

# def square_of_name_length(name):
#     counts = len([name]) #  This did not work because I am counting the number of eliments in a string and not the number of indexs in a string eliment.
#     return counts**2