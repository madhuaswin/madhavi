#finiding employ  basic salary employ name.
enum=int(input("enter the employ number"))
ename=input("enter the employ name")
basic_sal=int(input("enter the employ salaray"))
ensal=int(input("employ net salary"))
if(basic_sal<0):
    print("invalid salary it is not a employee")
else:
    if(basic_sal>=10000):
        da=basic_sal*(10/100)
        ta=basic_sal*(15/100)
        ma=basic_sal*(5/100)
        ha=basic_sal*(15/100)
    else:
        da=basic_sal*(20/100)
        ta=basic_sal*(15/100)
        ma=basic_sal*(10/100)
        ha=basic_sal*(30/100)
    print("-"*30)
    print("E M P L O Y S A l A R Y S L I P")
    print("="*30)
    netsal=basic_sal+da+ma+ta+ha
    print("{} employ number".format(enum))
    print("{} employ name".format(ename))
    print("{} employ basic_sal".format(basic_sal))
    print("="*30)
    print("{} employ da".format(da))
    print("{} employ ta".format(ta))
    print("{} employ ma".format(ma))
    print("{} employ ha".format(ha))
    #print("{} employ net salary".format(ensalary))
    print("-"*30)
        
        