class course():
    cost = 100
    duration = 60
    quizes = 4;

    def courseDescription(self):
        return ("The course costs %s doller for duration " \
                " %s hours and with %s quizes"%(str(self.cost),str(self.duration),str(self.quizes)))

courseObj = course()
print(courseObj.courseDescription())

courseObj.cost = 170
print(courseObj.courseDescription())