#programing demanstraton for outer loops.
i=1
while(i<4):
    print("*"*30)
    print("outer loop value={}".format(i))
    print("*"*30)
    j=1
    while(j<4):
        print("\tinner loop value={}".format(j))
        j=j+1
    else:
        print("inner loop excution over")
        print("*"*30)
        i=i+1
else:
    print("outer loop exicution over with while loop")
    