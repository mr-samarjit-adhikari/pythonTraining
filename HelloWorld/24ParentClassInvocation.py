
class Parent():
    def __init__(self,var):
        self.parentAttrib = var

class SubClass(Parent):
    def __init__(self,var):
        Parent.__init__(self,var)
        self.childAttrib = var


object = SubClass(10)
print("Value of parennt Attribute %d"%(object.parentAttrib))