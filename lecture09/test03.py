#Destructor

class DtiTest04:
    data1 = 10 

    def __init__(self,data2):
        self.data2 = data2 
        print ("L Sick")

    def doTask():
        print(":)")
    
    def dotask2(Value):
        print(Value)
    
    def __del__(self):
        print("Bye bye.....")

sauA=DtiTest04(20)
sauB=DtiTest04(30)
sauC=DtiTest04(20)

sauC.dotask2("T_T")
sauC.doTask()
print(sauA.data1 + sauB.data1)