
class myclass():

    def myfuncstion(self):
        print ("First Method")

    def myfunction2(self,strvar,numvar):
        print("Funcstion 2 got called with param "+strvar +" and "+str(numvar))



obj1 = myclass();
obj1.myfuncstion();
obj1.myfunction2("Test",16)

