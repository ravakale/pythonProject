#
#
#
# print("enter the limit")
# n=int(input())
# f=10
# i=10
# while(i<=n):
#     f=f*i
#     i=i+10
# print("the factorial answer is the ",f)
#
#
# k=0
# h=10
# while(h<=40):
#     k=k+h
#     h=h+10
# print("the addition is the ",k)
# o=h/4
# print("the divbide answer is the",o)


p=int(input("enter the number "))
d=0

for i in range(1,p+1):
    if(p%i==0):
        d=d+1

if(d==2):
    print("prime")
else:
    print("not p")