# In a function call, arguments must appear in this order: any positional arguments
#( value ); followed by a combination of any keyword arguments ( name=value ) and
#the *iterable form; followed by the **dict form.

def f(a,b,c):
    print (a,b,c)

#psitional
f(1,2,3)

#Keywords
f(a=2,b=1,c=6)

#Combination of position and keywords
f(1,c=3,b=2)

#Combination of keywords and defaults
def func(spam, eggs, toast=0, ham=0):
    print((spam, eggs, toast, ham)) # First 2 required

func(1, 2)
func(1, ham=1, eggs=0)
func(spam=1, eggs=0)
func(toast=1, eggs=2, spam=3)
func(1, 2, 3, 4)