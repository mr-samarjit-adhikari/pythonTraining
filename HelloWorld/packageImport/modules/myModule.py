
class MyIOError(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return repr(self.value)

def myOpen(filename,mode):
    try :
        with open(filename,mode) as file:
            pass
    except Exception as e:
        raise MyIOError(e)