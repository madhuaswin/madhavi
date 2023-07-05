#parmargumexm5
def offinfo(eno,ename,city="Irving"):
    print("\t{}\t{}\t{}".format(eno,ename,city))

print("="*50)
print("\teno\tename\tcity")
print("="*50)
offinfo(10,'Biden')
offinfo(ename='Trump',eno=20,city='Coppell')
offinfo(city='Plano',ename='Abort',eno=30)
print("="*50)