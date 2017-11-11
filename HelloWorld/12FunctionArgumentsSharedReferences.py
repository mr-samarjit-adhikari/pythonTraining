
def changer(a,b):    # Arguments assigned references to objects
    a = 2
    b[0] = 'spam';


X=1
L=[1,2]
changer(X,L)
print X,L

