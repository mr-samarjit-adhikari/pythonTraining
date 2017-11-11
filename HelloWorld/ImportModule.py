from MultipleInheritance import SubClass

instance1 = SubClass(10, 15);
instance2 = SubClass(20, 25);

print("Instance-1 attribX =%d" % (instance1.getAttribX()))
print("Instance-2 attribZ =%d" % (instance2.getAttribZ()))

if __name__ == '__main__':
    print ("HelloWorld !")
    print ("name is %s"%(__name__))