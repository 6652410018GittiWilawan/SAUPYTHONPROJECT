#คุณสมบัติ Encapsulation (ห่อหุ้มdata/attribute/field/property)
class DtiTest05:
    #data 
    infoA = 10 #ไม่ได้ Encap  
    __infoA = 20 #Encap ดูจาก __-------- เป็นการกำหนด access_modifier เป็น private

    def __init__(self,infoC,infoD) :
        self.infoC = infoC#ไม่ได้ Encap  
        self.__infoD = infoD #Encap ดูจาก __-------- เป็นการกำหนด access_modifier เป็น private

    #เมื่อใดก็ตาม Encap จะต้องมี Method 2 ตัวนี้เสมอ คือ get,set ของdata ตัวนั้น
    def setInfoB(self,infoB):
        self.__infoB = infoB

    def getInfoB(self):
        return self.__infoB
    
    def setInfoD(self, infoD):
        self.__infoD = infoD

    def getInfoD(self):
        return self.__infoD
    
    def showInfo(self):
        print(self.infoA, end='')
        print(self.__infoB, end='')
        print(self.infoC, end='')
        print(self.__infoD)
        print("-----------------------------------")

ob1 = DtiTest05(30,40)
ob2 = DtiTest05(30,100)
ob1.showInfo() #10 20 30 40
ob1.__infoA = 555
#ob1.__infoB = 999 #ไม่เปลี่ยนค่า เพราะมันถูก Encap
ob1.setInfoD(999)
ob1.showInfo() #10 999 30 40