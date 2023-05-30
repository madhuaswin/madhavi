#program for genarating table:
n=int(input("ENTER A NUMBER: "))
if(n<=0):
    print("invalid number")
else:
    for i in range(1,11):
        print("{} x {} = {}".format(n,i,n*i))
print("done exicuted")
        