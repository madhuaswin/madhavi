#programing for genarating table.
n=int(input("Which table do you want"))
if(n<=0):
    print("{} invalid number".format(n))
else:
    print("*"*30)
    print("T A B LES D I S P L A Y I N G")
    print("*"*30)
    s=1
    while(s<=15):
        print("{} * {} = {}".format(n,s,n*s))
        s=s+1
    else:
         print("*"*30)
    
    