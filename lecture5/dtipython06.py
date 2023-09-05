#คำสั่งReturn ที่ไม่มีอะไรต่อท้าย คือ การทำงานนั้นเสร็จแล้ว
def Holy1():
    print(111)
    print(222)
    return
    print(333)
    print(444)
    return

#Default Parameter มีการกำหนดค่าเริ่มต้นให้กับพารามิเตอร์
def dtitest(x,y,z=20,a = 10):
    print(f'{x}+{y}+{z}+{a} = {x+y+z+a}')

dtitest(5,100)

dtitest(9,8,10)