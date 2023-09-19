def borrowbro():
    borrowname = input("ป้อนชื่อผู้กู้: ")
    borrowprice = float(input("ป้อนจำนวนเงินที่กู้: "))
    return borrowname,borrowprice

def bronotreal(borrowprice):
    if borrowprice >= 1000:
        rate = borrowprice*2.5
    else :
        rate = borrowprice*5.5
    return rate

def plus(rate,borrowname):
    print(f"ชื่อผู้กู้{borrowname} จำนวนดอกเบี้ย{rate}บาท")

borrowname,borrowprice = borrowbro()
rate = bronotreal(borrowprice)

plus(rate,borrowname)