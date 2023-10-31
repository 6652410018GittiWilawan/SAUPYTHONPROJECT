class Dtitest01:
    pass

class DtiTest02:
    #data/attubute/property/field คือตัวประแปรประเภทหนึ่ง
    infoA = ""
    infoB = 1

    #method คือ ฟังก์ชั่นประเภทหนึ่ง
    def showHey(self) :
        print('Hey')

    def showInfoAInfoB(self):
        print(self.infoA)
        print(self.infoB)

#How to Create Object
objA = DtiTest02()
objB = DtiTest02()
sombat = DtiTest02()

objA.infoA = 'ImBetterThanYujiro'
objB.infoB = 9000

print(objA.infoB + objB.infoB)

sombat.showInfoAInfoB
