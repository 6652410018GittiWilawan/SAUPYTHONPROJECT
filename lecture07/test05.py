#List Function/Tuple Function 
# len(),min(),max()

var1 = [1,5,2,2,56,3,54,8,["Soy","Broki"],True,False,156498]

var2 = (1,23,23,24,5,35,3,24,2,(55,"Broki"),"มาลี","Hello")

print(f"ใน Var1 มีข้อมูลทั้งหมด {len(var1)}ข้อมูล")
print(f"ใน Var2 มีข้อมูลทั้งหมด {len(var2)}ข้อมูล")
#min กับ max ใช้ไม่ได้กับข้อมูลคนละชนิดกัน
#print(min(var1)) error
var3 = [10,20,30,True,10,20]
var4 = (10,20,30,True,10,20)
print(min(var3))
print(max(var4))