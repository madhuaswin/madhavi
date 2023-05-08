#program for genareting factorials.
n=int(input("Enter a number:"))
if(n<0):
    print("Invalid Number".format(n))
else:
    f=1
    for i in range(1,n+1):
        f=f*i
    else:
        print("factorial of{}={}".format(n,f))
    