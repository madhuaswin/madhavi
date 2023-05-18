#Separating odd even nubers from given list.
lst=[1,2,4,3,5,6,21,35,67,54,32,68,91,92,93,94,95,101,79,356,981,105]
print("*"*30)
print("given list")
print("*"*30)
for val in lst:
    print(val,end=" ")
print()    
print("*"*30)
print("list of even numbers:")
print("-"*30)
for val in lst:
    if(val%2==0):
        print(val)
else:
    print("*"*30)
    print("list of odd numbers:")
    print("*"*30)
    for val in lst:
        if(val%2!=0):
            print(val)
print("-"*30)        
        
    
    