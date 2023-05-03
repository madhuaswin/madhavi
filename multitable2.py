#program for genarating multitable.
n=int(input("Enter a number:"))
if(n<=0):
    print("{} invalid number".format(n))
else:
    print("*"*30)
    print("multitable".format(n))
    print("*"*30)
    i=1
    while(i<=15):
        
        print("{}*{} = {}".format(n,i,n*i))
        i=i+1
       
        
    else:
        print("displaying tables")
    