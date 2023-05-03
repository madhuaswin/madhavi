#genarating multitable
n=int(input("Enter a number"))
if(n<=0):
    print("{}invalid input".format(n))
else:
    print("*"*30)
    print("display the multitable".format(n))
    print("*"*30)
    i=1
    
     
    while(i<=10):
        print("{}*{}={}".format(n,i,n*i))
        i=i+1

    else:
        print("*"*30)
        print("finished displaying tables")
        print("*"*30)

              
    