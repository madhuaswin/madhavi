#separating odd numbers and even numbers.
n=[1,2,3,4,5,6,7,8,9,10,11,12]
print("given numbers:")
print("*"*30)
print("{}".format(n,end=""))
print()
print("*"*30)
print("EVEN NUMBERS:")
print("*"*30)
for val in n:
    if(val%2==0):
        print(val)
print("*"*30)
print("ODD NUMBERS:")
print("*"*30)
for val in n:
    if(val%2!=0):
        print(val)
print("*"*30)
print("odd and even numbers printed")
