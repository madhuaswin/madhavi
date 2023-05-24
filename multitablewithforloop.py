#multitable display.
#programing for genarating multitable using for loop.
n=int(input("Enter a number"))
if(n<0):
    print("{} invalid number".format(n))
else:
    print("*"*30)
    print("D I S P L A Y T A B L E S() ".format(n))
    print("*"*30)
    for i in range(1,11):
        print("{}*{}={}".format(n,i,n*i))
    else:
        print("*"*30)