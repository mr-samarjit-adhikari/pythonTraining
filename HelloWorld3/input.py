varinput = input("Enter the value:") # Get an input from someone stating Enter the value:

print (varinput ) # Print the obtained value

for x in range(5): #Looping the Input statement to get multiple values
    numbervar = "the number is "+str(input("Enter the "+str(x)+" number:"))
    print(numbervar)


#raw_input() is not supprted in python 3.x
#input works as raw_input()