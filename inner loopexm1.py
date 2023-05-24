#program for demonstratng inner loop.(using for loop)
for i in range (1,3):
    print("*"*30)
    print("outer loop value={}".format(i))
    print("*"*30)
    for j in range(1,4):
       print("\t inner loop of ={}".format(j))
    else:
        print("inner loop over")
        print("*"*30)
else:
    print("outer loop exicute over")