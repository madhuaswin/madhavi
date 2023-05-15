#separating addand even numbers.from given numbers.
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,55,70,81]
print("given numbers:")
print("*"*30)
for val in lst:
    print("val")
print("*"*30)
print("ODD NUMBERS:")
print("*"*30)
for val in lst:
    if(val%2)==0:
        print(val)
        continue
print("*"*30)
print("EVEN NUMBERS")
print("*"*30)
for val in lst:
    if(val%3)==0:
        print(val)
print("*"*30)
    