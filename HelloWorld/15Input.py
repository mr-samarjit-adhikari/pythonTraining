varinput = input("Enter the value:") # Get an input from someone stating Enter the value:
#Above will throw exceptin on input string as python
#Thus we need to use raw_input()
print (varinput ) # Print the obtained value

for x in range(5): #Looping the Input statement to get multiple values
    numbervar = "the number is "+str(input("Enter the "+str(x)+" number:"))
    print(numbervar)

varinput = raw_input("Enter the value:") #To covert a raw input into a string
print (varinput ) # Print the obtained value