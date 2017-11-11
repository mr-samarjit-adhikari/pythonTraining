
class Parent(object):
    def __init__(self):
        super().__init__()
        print("Inside the Parent Constructor")

    def setParentAttrib(self,var):
        self.parentAttrib = var

    def getParentAttrib(self):
        return self.parentAttrib


class AnotherParent(object):
    def __init__(self):
        super().__init__()
        print("Inside the AnotherParent Constructor")

    def setAnotherParentAttrib(self,var):
        self.anotherParentAttrib = var

    def getAnotherParentAttrib(self):
        return self.anotherParentAttrib


class SubClass(Parent,AnotherParent):
    def __init__(self):
        super().__init__()

    def setChildAttrib(self,var):
        self.childAttrib = var


object = SubClass()
print ("Method Resolution order -->"+str(SubClass.mro()))
object.setChildAttrib(10)
object.setParentAttrib(20)
object.setAnotherParentAttrib(30)

print("Parent attribute = %d "%(object.getParentAttrib()))
print("Another Parent attribute = %d "%(object.getAnotherParentAttrib()))