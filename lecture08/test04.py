class test04 : 
    data1 = 10

    # constructor
    def __init__(self,data2,data3):
        print("Yo....")
        self.data2=data2
        self.data3=data3

    #method member 
    def showSumdata(self):
        print(self.data1+self.data2+self.data3)
        self.ShowWow()
    
    def showwow(self):
        print('wow wow wow....')

objA = test04(20,30)
objB = test04(10,20)
objC = test04(20,100)
objD = test04(20,30)