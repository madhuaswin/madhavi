#Seperating values using with continue statement.
lst=[10,-10,20,-20,30,-30,40,-40,50,-50]
print("*"*30)
print("POSSITIVE NUMBERS:")
print("*"*30)
for val in lst:
    if(val<=0):
        continue
    print(val)
    
print("LIST OF NEGITIVE NUMBERS")
print("*"*30)
for val in lst:
    if(val>=0):
        continue
    print(val)


    