#program for demanstrating for loop in whileloop.
for i in range(5,0,-1):
    print("*"*30)
    print("outer loop value of= {}".format(i))
    print("*"*30)
    j=3
    while(j>0):
        print("\tinner loop value of={}".format(j))
        j=j-1
    else:
        print("inner loop complited")
else:
    print("*"*30)
    print("program exicuted")
