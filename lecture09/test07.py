import test06
import math
from test08 import calSquareArea ,calTriangleArea , calCircleArea

print(f'ผลรวมของ 10 + 20 = {test06.sumNumber(10,20)}')

test06.showHi()

print(f'ราคาสินค้า 20000 ภาษีเป็นเงิน {2000* test06.vat}')


print(f'7ยกกำลัง15มีค้า {math.pow(7,15)}')

print(f'พื่นที่วงกลมรัศมี3มีค่า{math.pi * math.pow(3,2)}')

print(f"พื้นที่วงกลม รัศมี 8 มีค่า {calCircleArea(8)}")


print(f"พื่้นที่สี่เหลี่ยม กว้าง10 ยาว5 มีค้า {calSquareArea(10,5)}")
