def ph(city, value):
    if 7 <= value <= 8:
        return "Result is Normal"
    elif value > 8:
        return "Result is Acid"
    else:
        return "Result is Alkali"

def get_user_input():
    city = input("ป้อนชื่อจังหวัด: ")
    value = float(input("ป้อนค่า pH: "))
    return city, value

def display(result):
    print(result)

def mainbro():
    city, value = get_user_input()
    result = ph(city, value)
    display(result)

mainbro()