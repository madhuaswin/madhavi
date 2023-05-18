#separating odd and even numbers.
num=[51,52,53,54,55,56,57,58,59,60,61]
print("*"*30)
print("DISPLAY NUMBERS:")
print("*"*30)
for val in num:
    print(val,end=" ")
print()
print("*"*30)
print("EVEN NUBERS")
print("*"*30)
for val in num:
    if(val%2==0):
        print(val)
print("*"*30)
print("ODD NUMBERS")
print("*"*30)
for val in num:
    if(val%2!=0):
        print(val)
print("*"*30)
        
        
        
