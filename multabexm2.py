#Displaying multi table with for loop
n=int(input("Enter a number"))
if(n<=0):
    print("Enter invalid Number")

else:
    for i in range(1,21):
        
        print("{}*{}={}".format(n,i,n*i))