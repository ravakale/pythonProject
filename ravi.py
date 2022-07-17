


class Runer:

    m="ravindra"
    n=90



    def __init__(self,a,b):
        self.aname=a
        self.amark=b

    @staticmethod
    def tune1(a):

        i=1
        f=1
        while(i<=a):
            print("this is the ouerride metjod in class one")
            f=f*i
            i=i+1

        return f

    @staticmethod
    def tune2(p):

        if(p>+18):
            print("you are the aplicble for vote")
        else:
            print("you are not aplicabkle for vote")


    @classmethod
    def tune3(cls):
        print(f"this class 2 methos {cls.m} and {cls.n}")

    def gun2(self):
        print(f"this is the value of {self.amark} and {self.aname}")



class Runer2(Runer):
    @staticmethod
    def tune1(a):
        i = 1
        f = 1
        print("this is ourride method in lass two")
        while (i <= a):

            f = f * i
            i = i + 1

        return f
    def __init__(self,a,b,c,d):
        super().__init__(a,b)
        self.aname2=c
        self.amark2=d

    def gun2(self):
        print(f"this is the value of {self.amark2} and {self.aname2}")




p=Runer2(21,43,56,43)

print("Enter the limit for factorial number")
a=int(input())
print(p.tune1(a))
print("Enter the age of any candite")
n=int(input())
p.tune2(n)
p.tune3()
p.gun2()



