var2 = (10,20,"Hello",(55,"Broki"),"มาลี","Hello")

#var2[2] = 'Hi' error
#การเปลี่่ยนแปลงค่า เพิ่ม ลบ ข้อมุลใน Tuple
#list(),tuple()
vartemp = list(var2)
vartemp[2] = 'Hi'
var2 = tuple(vartemp)
print(var2)