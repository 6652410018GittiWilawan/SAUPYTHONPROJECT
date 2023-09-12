def inputCarDetail():
    carNo = input('ป้อนทะเบียนรถ:')
    carweight = float(input("ป้อนน้ำหนักรถ:"))
    return carNo,carweight

def CheckCarAndShowWeight(carNo,carWeight):
    if carWeight>1000:
        print(f'ทะเบียนรถ{carNo}น้ำหนักไม่ผ่านเกณฑ์')
    else :
        print(f'ทะเบียนรถ{carNo}น้ำหนักผ่านเกณฑ์')

print("TruckChecker")
carNo,carweight = inputCarDetail()
print('-------------------')
CheckCarAndShowWeight(carNo,carweight)