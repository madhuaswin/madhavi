#listsumexam3
#finding the sum and avrage value using with empty list
n=int(input("How many values we have:"))
if(n<=0):
    print("Invalid input".format(n))
else:
    s=0
    for i in range(1,n+1):
        lst=list()
        val=float(input("{})Enter the value".format(i)))
        lst.append(val)
    else:
        print("*"*30)
        print("Display the elements")
        print("*"*30)
        for val in lst:
            print("print the value".format(val))
            s=s+val
        else:
            print("*"*30)
            print("sum of {}".format(s))
            print("AVG of {}".format(s/len(lst)))
            
        
    
        