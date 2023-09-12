def inputBaseHigh():
    base = float (input("ป้อนฐาน :"))
    high = float (input("ป้อนสูง :"))
    return base,high

def calAndShowTriangleArea(base,high):
    area = base * high / 2
    print(f'สามเหลี่ยมฐาน{base:.2f}สูง {high:.2f}มีพื้นที่ {area:.2f}')

print('CalculateTriangleArea')

base,high = inputBaseHigh()
print("------------------------------")
calAndShowTriangleArea(base,high)