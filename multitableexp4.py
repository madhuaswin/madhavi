#genararing multitables with for loop.
for n in range(1,21):
    print("="*30)
    print("multi tables : ({})".format(n))
    print("="*30)
    for i in range(1,11):
         print("{} x {} = {}".format(n,i,n*i))
            