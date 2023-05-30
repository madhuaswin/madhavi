#programing for genarating multitable.
lst=[2,3,4,5,6,-2,7,8,9,10,11,]
for n in lst:
    if(n<0):
        print("-"*30)
        print("invalid number")
        
    else:
        print("-"*30)
        print("MULTITABLE {}".format(n))
        print("-"*30)
        for i in range(1,11):
            print("{} x {} = {}".format(n,i,n*i))
    
        
    