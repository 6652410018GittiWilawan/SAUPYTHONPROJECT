def check_grades(id, name, grade):
    if grade < 2.00:
        return f"นักเรียน {name} รหัส {id} สอบไม่ผ่าน"
    else:
        return f"นักเรียน {name} รหัส {id} สอบผ่าน"

def input_student_data():
    id = input("ป้อนรหัสนักเรียน: ")
    name = input("ป้อนชื่อนักเรียน: ")
    grade = float(input("ป้อนเกรดเฉลี่ย: "))
    return id, name, grade

def bro():
    num_s = int(input("ป้อนจำนวนนักเรียน: "))

    for i in range(num_s):
        id, name, grade = input_student_data()
        result = check_grades(id, name, grade)
        print(result)
bro()