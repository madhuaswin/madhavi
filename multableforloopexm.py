#program for displaying tables using for loop.
n=int(input("enter a number:"))
if(n<0):
    print("{} invalid number".format(n))
else:
    
    for i in range(1,16):
        print("{}*{}={}".format(n,i,n*i))
    
