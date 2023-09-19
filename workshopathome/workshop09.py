def calculate_commission(sales):
    if sales <= 1000:
        commission = 0.0
    elif sales <= 2000:
        commission = sales * 0.01
    elif sales <= 3000:
        commission = sales * 0.03
    else:
        commission = sales * 0.05
    return commission

def get_user_input():
    id = input("ป้อนรหัสพนักงาน: ")
    name = input("ป้อนชื่อพนักงาน: ")
    sales = float(input("ป้อนยอดขาย (บาท): "))
    return id, name, sales

def display_result(id, name, sales, commission):
    print(f"รหัสพนักงาน: {id}")
    print(f"ชื่อพนักงาน: {name}")
    print(f"ยอดขาย: {sales} บาท")
    print(f"ค่าคอมมิชชัน: {commission} บาท")

def main():
    id, name, sales = get_user_input()
    commission = calculate_commission(sales)
    display_result(id, name, sales, commission)

main()