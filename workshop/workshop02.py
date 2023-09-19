def studentname():
    studentcode = input ("ป้อนรหัสนักเรียน: ")
    student = input ("ป้อนชื่อนักเรียน: ")
    return studentcode,student
def TestScore():
    Test1 = float(input("ป้อนคะแนนสอบครั้งที่1 :"))
    Test2 = float(input("ป้อนคะแนนสอบครั้งที่2 :"))
    Test3 = float(input("ป้อนคะแนนสอบครั้งที่3 :"))
    return Test1,Test2,Test3
def All(studentcode,student,test1,test2,test3):
    Cal = (test1+test2+test3)/3
    print (f"รหัสนักเรียน{studentcode} ชื่อ{student} ได้คะแนนรวม{Cal}")

studentcode,student = studentname()
Test1,Test2,Test3 = TestScore ()
All(studentcode,student,Test1,Test2,Test3)