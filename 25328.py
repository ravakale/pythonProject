
class Manager:

    def __init__(self,aname1,amark1):
        self.name=aname1
        self.mark=amark1
        print("i am the con of class1")

    def con1(self):
        print(f"this is the class 1{self.name}and the mark is the{self.mark}")







class Manager2(Manager):

    def __init__(self,aname2,amark2):

        self.name = aname2
        self.mark = amark2
        print("i am, the con of class 2")
    def con2(self):
            print(f"this is the class 2{self.name}and the mark is the{self.mark}")






ravi=Manager2(12,23)

ravi.con1()
ravi.con2()




