
class member():
    """
    Parent/Child class in java/C++ pattern
    """
    def __init__(self):
        self.username = None
        self.password = None
        self.uid      = None
        print("Inside member constructor")

    def setUserName(self,username):
        self.username  = username

    def setPassword(self,password):
        self.password = password

    def setUid(self,uid):
        self.uid = uid;

    def getUserName(self):
        return self.username

    def getPassword(self):
        return self.password

    def getUid(self):
        return self.uid

class PaidMember(member):
    """
    subclass of parent
    """
    def __init__(self):
        super().__init__()
        self.cardInfo = None
        self.status   = None
        print("Inside PaidMember Costructor")

    def setCardInfo(self,cardStr):
        self.cardInfo = cardStr

    def setStatus(self,status):
        self.status = status

    def getCardInfo(self):
        return self.cardInfo

    def getStatus(self):
        self.set
        return self.status


if __name__=='__main__':
    """
    This is a unit test way
    """
    paidMem = PaidMember()


