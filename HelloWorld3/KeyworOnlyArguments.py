#keyword-only arguments—arguments that must be passed by keyword only and will
#never be filled in by a positional argument. This is useful if we want a function to both
#process any number of arguments and accept possibly optional configuration option

def kwonly(a, *b, c):
    print(a, b, c)

kwonly(1, 2, c=3)
kwonly(a=1, c=3)
#kwonly(1, 2, 3)  #TypeError: 3rd Argument is not of form c=3

#We can also use a * character by itself in the arguments list to indicate that a function
#does not accept a variable-length argument list but still expects all arguments following
#the * to be passed as keywords.

def keyWonly(a, *, b, c):
    print(a, b, c)

keyWonly(1, c=3, b=2)
keyWonly(c=3, b=2, a=1)
keyWonly(1, 2, 3)  #??
keyWonly(1) #??