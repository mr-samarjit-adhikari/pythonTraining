def myfunctions(num1):  # defining functions with arguments
    print("This is the number" + str(num1))
    return "This is the number" + str(num1)


def myfunctionadd(*arg):  # defining functions with arguments as tuple
    added = 0
    for x in arg:
        added = added + x
    return added


print("Out of function")
a = 10

print(myfunctions)  # printing the function as object

print(myfunctions(a))  # calling function with variable as argument

print(myfunctionadd(1, 2, 3, 4, 5, 6, 7, 8,9))  # calling function with list as argument