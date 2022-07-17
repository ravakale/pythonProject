
import time
import a as a

import datetime
class op:
    def cakk(self):
        f = open("text.txt", "r")
        con = f.read()
        print(f"\n{con}")
        f.close()
        print("plese wait.....")

class po:

    def bank(self):
        print("welcome")
        print("Dear ravindra kale")
        d=datetime.datetime.now()
        print(f"your entry date is\t {d.date()}")
        print(f"your entry time is\t{d.time()}")

        print("serching your data plese wait....")
        time.sleep(8)


        r=op()
        r.cakk()
        time.sleep(10)

        print("select your otion you want to do it\n")
        print("\n1.chech balance\n2.Number update\n3.Aadhar link\n4.money deposit\n5.money credit\n6.Apply for ATM card")
        g=int(input())
        if(g==1):
            if(a==13598100013951):
                print("plese wait....")
                time.sleep(3)
                print("your balance is=9324")
        elif(g==2):
             print("Enter your mobile number if you wat to link")
             n=int(input())
             if(n!=7028751114):
                 print("this number is olredy link")
             elif(n==9067649624):
                 print("plese enter OTP")
                 ot=int(input())
                 if(ot==1234):
                     print("your number link succesfully")

        elif(g==3):
            print("\n1.check Aadhar status\n2.link your Aadhar ")
            k=int(input())
            if(k==1):
                print("No aadhar link this acount")

            elif(k==2):
                print("Enter aadhar number")
                l=int(input())
                if(l==825077223256):
                    print("your aadhar number is link sucses fully")
                else:
                    print("plese enter correct aadhar number")
        elif(g==4):
            print("Enter amount if want you deposit")
            h=int(input())
            if(h==5000):
                print("your amount is deposit")
            elif(h==10000):
                print("your amount is deposit")
            elif(h==50000):
                print("your amount is deposit")
            elif(h==20000):
                print("your amount is deposit")
            else:
                print("enter amount is not corect")
        elif (g == 5):
                print("Enter amount if want you credit")
                h = int(input())
                if (h == 5000):
                    print("your amount is credit")
                elif (h == 10000):
                    print("your amount is credit")
                elif (h == 50000):
                    print("your amount is credit")
                elif (h == 20000):
                    print("your amount is credit")
                else:
                    print("enter amount is not corect")

        elif(g==6):
            print("if u want to apply ATM card ")
            print("write application for ATM card")
            ch=(input())
            f=open("ravi.txt","w")
            f.write(ch)
            f.close()
            print("plese wait....your aplication loaded")
            time.sleep(4)
            f=open("ravi.txt","r")
            y=f.read()
            print(y)

    def num(self):
        print("Dear mahesh kale")


    def mum(self):
        print("welcome")
        print("Dear mahesh kale")

    def om(self):
        print("welcome")
        print("Dear omkar kale")


if __name__ == '__main__':

    print("welcome in bank baroda")
    time.sleep(2)
    print("Enter your 14-digit passbook number")
    a=int(input())
    p=po()
    if(a==13598100013951):

      p. bank()

    elif(a==13598100013952):

     p.num()
    elif (a == 13598100013953):

     p.mum()
    elif (a == 13598100013954):

     p.om()
    else:
        print("plese enter corrct passbook number")
        time.sleep(1)
        print("bank not found this acount number")
        print("plese try again")