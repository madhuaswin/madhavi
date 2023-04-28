#genrating multitable
n=int(input("Enter a number"))
if(n<=0):
    print("it is invalid".format(n))
else:
    print("*"*30)
    print("Displaying multitable".format(n))
    print("*"*30)
    i=1
    while(i<=10):
        print("{}*{}={}".format(n,i,n*i))
        i=i+1
    else:
        print("*"*30)
        
    
    