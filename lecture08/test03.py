# OOP
# Camel case, snake case
class DtiSau :
    # data/property member
    stu_name = ''
    score = 0 
    gpa = 0

    # method member คืือการทำงาน
    def hiStudent(self):
        print(f'สวัสดี{self.stu_name}')

    def ShowScoreAndGrade(self):
        print(f'คะแนน{self.score} ได้เกรด {self.gpa}')

# สร้าง Object
obj1 = DtiSau() #ชื่อคลาสที่มี() เราเรียกว่าเป็นการสั่งให้ Constructor ของคลาสทำงาน
obj2 = DtiSau()

obj1.stu_name = 'สมBro'
obj1.hiStudent()
obj2.stu_name = 'สมsis'
obj2.score = 99
obj2.gpa = 3.99