#The last two matching extensions, * and ** , are designed to support functions that take
#any number of arguments.

def f(*args): print(args)

#When this function is called, Python collects all the positional arguments into a new
#tuple and assigns the variable args to that tuple. Because it is a normal tuple object, it
#can be indexed, stepped through with a for loop, and so on:

f()

f(1)

f(1,2,3,4)


def func(**args):
    """
    Comments
    """
    print(args)

func()

func(a=1,b=2)

# Combination of * and **
def demoFunction(a, *pargs, **kargs):
    print(a, pargs, kargs)

demoFunction(1, 2, 3, x=1, y=2)

#Unpacking arguments.

#In recent release we can use the * syntax when we call a function
def unpackFunc(a, b, c, d):
    print(a, b, c, d)

args = (1, 2)
args += (3, 4)
unpackFunc(*args)    # Same as unpackFunc(1, 2, 3, 4)

args = {'a': 1, 'b': 2, 'c': 3}
args['d'] = 4
unpackFunc(**args)  # Same as unpackFunc(a=1, b=2, c=3, d=4)

unpackFunc(*(1, 2), **{'d': 4, 'c': 3})  # Same as func(1, 2, d=4, c=3)
unpackFunc(1, *(2, 3), **{'d': 4})       # Same as func(1, 2, 3, d=4)
unpackFunc(1, c=3, *(2,), **{'d': 4})    # Same as func(1, 2, c=3, d=4)
unpackFunc(1, *(2, 3), d=4)              # Same as func(1, 2, 3, d=4)
unpackFunc(1, *(2,), c=3, **{'d':4})     # Same as func(1, 2, c=3, d=4)