def greeting(username): # github test 2
    return 'hello ' +         username +'!'

def add(x=0,y=0,z=0):
    return x+y+z

def add10(x):
    return x+10

def square(x):
    return x**2

def sum_of_squares(x):
    return add(square(x), square(x))

def sum_of_squares2(x):
    square_of_x=square(x)
    return add(square_of_x, square_of_x)