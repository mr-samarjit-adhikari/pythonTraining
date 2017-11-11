
class constructorDemo(): #No Class variables. Only object variables
    name = "ABCD"
    age  = 100
    def __init__(self,name,age):
        self.name = name
        self.age  = age
        print("Inside consturctor with name %s and age %s"%(str(name),str(age)))

    def printMyInfo(self):
        print("Name :%s Age =%d"%(self.name,self.age))

object = constructorDemo('samarjit',33);
object.printMyInfo()
object.name = "XYZ"
object.age = 333
print object.name,object.age
object.printMyInfo()