def users():
    user = int(input("ป้อนตัวเลขที่ต้องการทาย: "))
    return user

def binbro(user):
    correct_number = 25
    if user == correct_number:
        return True
    else:
        return False

def winner():
    print("Correct, You are the winner")

def loser():
    print("Not Correct !!!")

def bingogay():
    user = users()

    if binbro(user):
        winner()
    else:
        loser()

bingogay()