class DtiTest03 :
    #data
    infoA = 10
    #Contructor จะเป็นตัวทำให้ OBJ ที่สร้างจากคลาสเดียวกันไม่จำเป็นต้องเหมือนกัน
    def __init__(self,infoB,infoC):
        self.infoB = infoB
        self.infoC =- infoC
        print('OMG OMG OMG')

    #method
    def showMixAndInfo(self, mix):
        print(self.infoA + self.infoB + self.infoC + mix)

#OBJ
sau1 = DtiTest03(20 , 30 )
sau1 = DtiTest03(10 , 100 )
sau1 = DtiTest03(30 , 40 )