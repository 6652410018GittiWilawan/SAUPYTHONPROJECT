#list Method
var1 = [10,20,'Hello',True,[111,'soy'],"mabro"]

#append เพิ่ม1ข้อมูล
var1.append(555)
var1.append(["Hi","Ho",240])
print (var1)

#extend เพิ่่มแต่ล่ะข้อมูล
var1.extend([10,20,30])
print (var1)

#remove
var1.remove('Hello')
print(var1)

var2 = [10,20,"Hello"]

#insert
var2.insert(2,"Bro")
print(var2) # [10,20,Bro,Hello]

#pop
var2.pop()
print(var2)#[10,20,Bro]
var2.pop(1)
print(var2)

#index
print(var2.index("Bro"))

#count นับจำนวนข้อมูลนั้นๆ ที่ซ้ำอยู้ใน List มีกี่ตัว
print(var1.count(10))
var3=[10,10,20,"hi",10,"hi"]
print(f'ในvar3 มีHiทั้งหมด{var3.count("hi")}ตัว')

#Method ต่อไปนี้ใช้ได้เฉพาะข้อมูลที่เป็นประเภทเดียวกันเท่านั้น
#sort
var4 = [10,10,20,"Hi",10,"Hi"]
#var4.sort()Error
var5 = [99,34,635,343,99]
print(var5)
var5.sort()
print(var5)
var5.sort(reverse=True)
print(var5)

