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
    return dif(sum_1,sum_2)