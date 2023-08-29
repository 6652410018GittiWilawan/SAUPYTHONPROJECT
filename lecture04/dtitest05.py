def func(month) :
    sell =  month - (month * 7/100)-500
    return sell
name_code = input ("ป้อนรหัสพนักงาน : ")
name = input ("ป้อนชื่อพนักงาน : ")
emoployeemoney = float(input("ป้อนเงินเดือนพนักงาน : "))
sell = func(emoployeemoney) 

print(f"ชื่อของคุณคือ {name} รหัสของคุณคือ {name_code} เงินเดือนของคุณคือ{sell}บาท")