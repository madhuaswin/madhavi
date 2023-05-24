#program genarating employ pay slip,
ename=input("Employ NAME:")
enum=int(input("EMPLOY NUMBER:"))
basicsal=float(input("ENTER EMPLOY BASIC SALARY"))
if(basicsal<0):
    print("{}is invalid salary".format(basicsal))
else:
    if(basicsal>=20000):
        ta=basicsal*(10/100)
        da=basicsal*(20/100)
        ma=basicsal*(2/100)
        lic=basicsal*(2/100)
    else:
        ta=basicsal*(8/100)
        da=basicsal*(5/100)
        ma=basicsal*(1/100)
        lic=basicsal*(1/100)
    basicsal=ta+da+ma+lic
    print("-"*30)
    print("EMPLOY PAY SLIP")
    print("*"*30)
    print("{} enter employ name".format(ename))
    print("{} enter employ number".format(enum))
    print("{} enter employ basic salary".format(basicsal))
    print("{} employ ta".format(ta))
    print("{} employ da".format(da))
    print("{} employ ma".format(ma))
    print("{} employ lic".format(lic))
print("This is complete employ salary information.")