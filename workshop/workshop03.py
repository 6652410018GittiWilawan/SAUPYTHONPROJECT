def price():
    name = input("ป้อนชื่อสินค้า: ")
    broprice = float(input("ป้อนราคาสินค้า: "))
    return name,broprice
def CalTax(name,broprice):
    Cal = broprice * 7/100
    All = print(f"ชื่อสินค้า{name}ราคา{broprice}บาท ภาษีที่ได้ราคา{Cal}บาท")

name,broprice = price()
CalTax (name,broprice,)