def calculate1(minutes):
    return minutes * 5

def calculate2(minutes):
    return minutes * 3

def calculate3(minutes):
    return minutes * 1.5

def phone(minutes):
    if 1 <= minutes <= 15:
        return 1(minutes)
    elif 16 <= minutes <= 30:
        return calculate2(minutes)
    elif minutes >= 31:
        return calculate3(minutes)
    else:
        return 0

def bro():
    try:
        name = input("ชื่อผู้ใช้โทรศัพท์: ")
        phone_number = input("เบอร์โทรศัพท์: ")
        minutes = int(input("จำนวนนาทีที่ใช้โทร: "))

        cost = phone(minutes)
        print(f"ค่าโทรศัพท์ที่ต้องจ่ายคือ: {cost} บาท")
    except ValueError:
        print("โปรดป้อนจำนวนนาทีเป็นตัวเลข")

bro()