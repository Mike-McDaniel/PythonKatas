


# 					mapping functions
# a[N] -> b[N]
# transforming a list = "mapping" a list
# map = output list is always the same length as the input list

def XaddTenToAll(numbers):
	new_numbers = [] 				# seed
	for x in numbers:				# loop
		new_numbers.append(x + 10)	# condition
	return new_numbers				# return the accumulate

def XfirstLetters(names):
	new_names= []
	for name in names:
		new_names.append(name[0])
	return new_names

def XoddOrEven(numbers):
	newNumbers = []
	for number in numbers:
		if number % 2 == 1:
			newNumbers.append("odd")
		else: 
			newNumbers.append("even")
	return newNumbers

def XoddOrPlus10(numbers):
	newNumbers = []
	for number in numbers:
		if number % 2 == 1:
			newNumbers.append("odd")
		else:
			newNumbers.append(number + 10)
	return newNumbers

def XlengthOfString(strings):
	lengths = []
	for string in strings:
		lengths.append(string + ": " + str(len(string)))
	return lengths



# 					filter functions
# must have an if statement (conditional and combination logic)
# a[N] -> a[0-N]
# return empty to N items, where N is the length of the list

def XonlyOdds(numbers):
	newNumbers = [] 				  # seed
	for number in numbers: 			  # loop
		if (number % 2) == 1: 		  # conditional
			newNumbers.append(number) # combination logic
	return newNumbers 				  # return the accumlate

def XstartsWithS(names):
	newNames = []
	for name in names:
		if name[0] == "S":
			newNames.append(name)
	return newNames

def XonlyEvenStrings(strings):
	evens = []
	for string in strings:
		if len(string) % 2 == 0:
			evens.append(string)
	return evens


# 					reduce functions
# a[N] -> b
# collapsing a list into a single thing
# expanding a list into a many things

def XsumList(numbers):
	total = 0 				   # seed
	for number in numbers: 	   # loop
		total = total + number #condition
		# 0 + 1 -> 1
		# 1 + 1 -> 2
		# 2 + 1 -> 3
		# 3 + 2 -> 5
	return total 			   # return the accumulate

def XconcatLetters(letters):
	name = ""
	for letter in letters:
		name = name + letter # adding to the right of the seed
			   				 # position matters (positional)
	return name

def XreverseStrings(letters):
	name = ""
	for letter in letters:
		name = letter + name # adding to the left of the seed
			   				 # position matters (positional)
	return name

def XduplicateLetters(letters):
	dupstring = ""
	for letter in letters:
		dupstring = letter + dupstring + letter # (positional)
					# "a"  +    ""     +   "a"  ->   "aa"
					# "b"  +   "aa"    +   "b"  -> 	"baab"
					# "c"  +  "baab"   +   "c"  -> "cbaabc"
	return dupstring # return accumulate = "cbaabc"


#                   exercise 1
# could be any kind of function (map, filter, reduce).
# steve write test, mike build function

# how to start a function before building the loop and condition
# 			\/\/\/
# def functionname(perameter): 
	# seed = []
	# return seed

def XcountLetters(names): # (mapping)
	counts = []       			 # seed
	for name in names: 			 # loop
		counts.append(len(name)) # condition
	return counts     			 # return accumulate

def XmysteryMath(numbers): # (mapping)
	mm = []
	for number in numbers:
		mm.append(number / 5)
	return mm

def XfirstNLast(names): # (mapping)
	fNL = []
	for name in names:
		fNL.append(name[0] + name[len(name)-1])
	return fNL


#                   exercise 2
# self written tests and functions


def Xsquare_of_name_length(names): # (mapping)
    counts = []
    for name in names:
        counts.append(len(name)**2)
    return counts

def Xsquare_of_single_name_length(name): #(mapping)
    counts = len(name)
    return counts**2

def Xsquare_of_name_length(names): # (mapping)
    counts = []
    for name in names:
        counts.append(Xsquare_of_single_name_length(name))
    return counts