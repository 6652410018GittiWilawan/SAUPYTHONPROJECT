#คุณสมบัติเด่น Inheritance สืบทอด คือ การที่คลาสหนึ่ง สือทอดอีกคลาสหนึ่ง ***(re-use)
#สือทอดมีแม่(super class) มีลูก (super class)
#แม่มีไร ลูกมีอันนั้น เมื่อมีการสืบทอด (Inheritance)

#คุณสมบัติเด่น Polymorphism (พ้องรูป) คือ การที่คลาสลูก มาเเปลงเป็นMethodคลาสแม่มาเขียนใหม่

class Sau01 : 
    infoA = 10 

    def showHi():
        print("Hi-------")

class Sau02(Sau01) : # Inheritance
    infoB = 20 

    def showHey():
        print("Hey.................")

    #overidingmethod :Polymorphism
    def showHi():
        print("Hi-------------------------")

ob1 = Sau01()
ob2 = Sau02()
ob2.showHi()