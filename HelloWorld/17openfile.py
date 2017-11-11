
files1 = open('textFile.txt','r');
files2 = open('textFileWrite','a+')

#print (files1.read())

#Read by line by l  ine
for line in  files2.readlines():
    print (line)

files2.write("Creating a file for demo\n")

files1.close()
files2.close()