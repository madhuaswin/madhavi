#argumparmtrs3
def disstuinfo(sno,sname,marks,addr="HYD",occp="Stu"):
    print("\t{},\t{},\t{},\t{},\t{}".format(sno,sname,marks,addr,occp))

#main program
print("="*50)
print("\tsno\tsname\tmarks\tAdderss\toccp")
print("="*50)
disstuinfo(1,'Asish',75)#fuction call
disstuinfo(2,'shrith',50)#fuction call
disstuinfo(3,'Ashu',95)#fuction call
disstuinfo(4,'madhu',70,'Irving')#fuction call
disstuinfo(5,'priya',60)#fuction call
disstuinfo(6,'Anusha',80,'Guntur')
print("="*50)

