#finding student no stn name..
sceince=0
maths=0
eng=0
elr=0
sname=input("Enter the student name")
sno=int(input("Enter the serial number"))
bmarks=int(input("Enter student basic marks"))
if(bmarks<35):
    print("student failed in exams")
else:
    if(bmarks>90):
        sceince=bmarks*(45/100)
        maths=bmarks*(70/100)
        eng=bmarks*(60/100)
        elr=bmarks*(50/100)
        print("-"*30)
print("S T U D E N T R E P O R t C A R D")
print("="*30)
totalmarks=bmarks+sceince+maths+eng+elr
print("{} enter the student name".format(sname))
print("{} enter the serial number".format(sno))
print("{} enter the basic marks".format(bmarks))
print("*"*30)
print("{} student scenice".format(sceince))
print("{} student maths".format(maths))
print("{} student eng".format(eng))
print("{} student elr".format(elr))




        