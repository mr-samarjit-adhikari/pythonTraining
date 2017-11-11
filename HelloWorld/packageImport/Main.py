
from packageImport.modules.myModule import *

try:
    fileObj = myOpen("textFile","r")
except MyIOError as e:
    print ("Exception with %s"%(e.value))