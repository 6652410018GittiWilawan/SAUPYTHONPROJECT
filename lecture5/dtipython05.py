def Func1() :
    Money = float(input("ป้อนเงิน :"))
    person = int(input("ป้อนคน :"))
    return Money,person

def Func2(Money,person,) : 
    Humnoiy = format(float(Money),".2f")
    print(f"จำนวนเงิน {Money:.2f} บาท คน {person} คน แชร์กันคนละ {round(Money/person)}บาท")
    print("จำนวนเงิน",Humnoiy,"บาท","คน",person,"คน","แชร์กันคนละ",round(Money/person),"บาท")
    print("จำนวนเงิน"+str(Humnoiy)+"บาท"+"คน"+str(person)+"คน"+"แชร์กันคนละ"+str(round(Money/person))+"บาท")
    print("จำนวนเงิน {:.2f} บาทคน {} คนแชร์กันคนละ{}บาท".format(Money,person,round(Money/person)))
    print("จำนวนเงิน %.2f บาทคน %d แชร์กันคนละ %d บาท"%(Money,person,round(Money/person)))
Money,person, = Func1()

Func2(Money,person,)

    