try :
    num1 = int(input("input numbe1 :"))
    num2 = int(input("input numbe2 :"))

    result1 = num1 * num2
    result2 = num1 / num2
   
    print('{} x {} = {} '.format(num1,num2,result1))
    print('{} ÷ {} = {} '.format(num1,num2,result2))
except ValueError :
    print("ตรวจสอบการป้อนข้อมูล ป้อนได้แค่ตัวเลขเท่านั้น")
except ZeroDivisionError : 
    print("ตรวจสอบการป้อนข้อมูล ตัวเลขตัวที่ 2 ห้ามเป็น 0")
except Exception:
    print("มีข้อผิดพลาดเกิดขึ้น กรุณาติดต่อ 08******** ทีม IT ")
finally :
    print ("OH")