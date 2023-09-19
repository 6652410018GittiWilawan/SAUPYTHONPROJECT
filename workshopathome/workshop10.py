def welcome_freshman():
    return "Welcome Freshman"

def welcome_sophomore():
    return "Welcome Sophomore"

def welcome_junior():
    return "Welcome Junior"

def welcome_senior():
    return "Welcome Senior"

def main():
    try:
        year = int(input("ป้อนชั้นปี 1-4: "))
        
        if year == 1:
            message = welcome_freshman()
        elif year == 2:
            message = welcome_sophomore()
        elif year == 3:
            message = welcome_junior()
        elif year == 4:
            message = welcome_senior()
        else:
            message = "โปรดใส่เลข1-4"
        
        print(message)
        
    except ValueError:
        print("โปรดใส่เลข1-4")

main()