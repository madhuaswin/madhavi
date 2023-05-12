#creating a empty list and finding values.
n=int(input("Enter how many values we have:"))
if(n<=0):
    print("invalid input".format(n))
else:
    s=0
    lst=list()
    for i in range(1,n+1):
        val=int(input("{}.Enter the value:".format(i)))
        lst.append(val)
    else:
        print("*"*30)
        print("Display the elements")
        print("*"*30)
        for val in lst:
            print(" value{}".format(val))
            s=s+val
        else:
            print("*"*30)
            print("sum of {}".format(s))
            print("AVG of {}".format(s/len(lst)))
            print("*"*30)
            
        
    