
def disk(function):
    function()
    print "and a disk"



@disk
def computer():
    print ("This is computer")

if __name__ == '__main__':
        computer
        #computer_disk()