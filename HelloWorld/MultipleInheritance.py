
class ParentClass():
    def __init__(self,varX=300,varZ=400):
        self.attribX = varX
        self.attribZ = varZ

    def getAttribX(self):
        return self.attribX;

    def getAttribZ(self):
        return self.attribZ;


class AnotherParentClass():
    def __init__(self, varW=100, varZ=200):
        self.attribW = varW
        self.attribZ = varZ

    def getAttribW(self):
        return self.attribW;

    def getAttribZ(self):
        return self.attribZ;


class SubClass(ParentClass, AnotherParentClass):
    def __init__(self,varX,varY):
        ParentClass.__init__(self,varX,varY)
        AnotherParentClass.__init__(self,varX,varY)
        self.attribX = varX;
        self.attribY = varY;
        print ("SubClass name is %s" % (__name__))

    def getAttribX(self):
        return self.attribX;

    def getAttribY(self):
        return self.attribY;

if __name__ =='__main__':
    instance1 = SubClass(10,15);
    instance2 = SubClass(20,25);

    print("Instance-1 attribX =%d" %(instance1.getAttribX()))
    print("Instance-2 attribZ =%d" % (instance2.getAttribZ()))