var1 = [10,20,"Hello",["Soy","Broki"],True,False,156498]

var2 = var1
var3=var1.copy()

print (var3)
print (var2)
print (var1)
print("-----------------------")
var2[0]= 111
print (var3)
print (var2)
print (var1)
print("-----------------------")
var3[0] = 999
print (var3)
print (var2)
print (var1)
print("-----------------------")