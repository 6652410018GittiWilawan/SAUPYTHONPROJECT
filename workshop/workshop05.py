def bro():
    codebro = input("ป้อนรหัสพนักงาน: ")
    namebro = input("ป้อนชื่อพนักงาน: ")
    monthneybro = float(input("ป้อนเงินเดือน: "))
    return codebro,namebro,monthneybro
def tax():
    tax7 = 0.07*monthneybro
    realtax = monthneybro - tax7
    truetax = realtax - 500
    return tax7,realtax,truetax

def minustax(truetax,codebro,namebro): 
    print (f"พนักงาน{namebro}รหัส{codebro}")
    print (f"เงินเดือนสุทธิ {truetax} บาท")

codebro,namebro,monthneybro = bro()
tax7,realtax,truetax = tax()
minustax(truetax,codebro,namebro)


    