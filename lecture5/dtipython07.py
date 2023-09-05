import math
radius = float(input("ป้อนค่ารัศมีของวงกลม: "))
#calAreaCircle
area = math.pi * radius**2
#calRoundCircle 
round = 2 * math.pi * radius
#calCubeCircle
volume = (4/3) * math.pi * radius**3

def ShowResult ():
    print(f"พื้นที่วงกลมเป็น: {area:.4f} เส้นรอบวงเป็น: {round:.4f} ปริมาตรทรงกลมเป็น: {volume:.4f}")

ShowResult()

#calAreaCircle
#def calAreaCircle(r) :
    #area = math.pi * r **2
    #area = math.pi * r * r
    #area = math.pi * math.pow(r,2)
    #return area
    #return math.pi * math.pow(r,2)
