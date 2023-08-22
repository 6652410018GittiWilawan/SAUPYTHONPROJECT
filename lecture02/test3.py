Emp_Name = input('ป้อนชื่อพนักงาน : ')
Sale_price =input("ป้อนยอดขาย : ")
print('---------------------')
#ฟังก์ชั่นแปลงStringเป็นNumber  --------->  int() , float()
Commission = float(Sale_price) * 10/100  

print('คุณ {} ยอดขาย {} บาท ได้ค่าตอบแทน {} บาท '.format(Emp_Name,Sale_price,Commission))
print(f'คุณ {Emp_Name} ยอดขาย {Sale_price} บาท ได้ค่าตอบแทน {Commission}บาท')
print("คุณ",Emp_Name,"ยอดขาย",Sale_price,"บาท ได้ค่าตอบแทน",Commission,"บาท")
print(str("คุณ")+str(Emp_Name)+str("ยอดขาย")+str(Sale_price)+str("บาท ได้ค่าตอบแทน")+str(Commission)+str("บาท"))