#program for diplay sum and avarage.
lst=[20,13,15,18,35,45]
print("-"*30)
print("Display the elements:")
print("-"*30)
s=0
for val in lst:
    print("\t{}".format(val))
    s=s+val
else:
    print()
    print("-"*30)
    print("sum={}".format(s))
    print("Avg={}".format(s/len(lst)))
    print("-"*30)
