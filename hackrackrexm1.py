#Given an integer, , perform the following conditional actions:

#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of 6 to 20 , print Weird
#If n is even and greater than 20, print Not Weird
n=int(input("enter a number:"))
if(n%2!=0):
    print("Weird")
else:
    if n in range(2,5):
        print("Not Weird")
    elif(n>=6)and(n<=20):
        print("Weird")
    elif(n>20):
        print("Not weird")       
    

