def func(cost) :
    sell = cost + (cost * 10 / 100)
    return sell
name = input("ป้อนชื่อสินค้า : ")
cost = float(input("ป้อนราคาต้นทุน : "))

sell = func(cost)

print(f"ราคาของ {name} คือ {sell} บาท")