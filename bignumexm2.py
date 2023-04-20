#bigexam2
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
#a=200 b=100 c=50
big=a
if(a>b)and (a>c):
    print("{} big number".format(a))
if(b>a)and (a>b):
    print("{} big number".format(b))
if(c>a)and (c>b):
    print("{} big number".format(c))

print("~"*30)
print("this is the big number")
