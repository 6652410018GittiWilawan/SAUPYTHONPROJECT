def X():
    xx = float(input("ป้อนค่า x: "))
    return xx
def y2():
    y = 2*(xx)**2+2*(xx)+1
    return y
def all (xx,y):
    print(f"X มีค่า{xx}แก้สมการYได้{y}")

xx = X()
y = y2()
all(xx,y)
