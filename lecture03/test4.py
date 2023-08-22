Money = input("ป้อนจำนวนเงิน : ")
People = input("ป้อนจำนวนคน :")
print("------------------------------------")
Flo = float(Money) / float(People)

print("เงิน {} แบ่งคนเป็นจำนวน {} คนได้คนล่ะ {} บาท ".format(Money,People,Flo))
print(f"เงิน {Money} แบ่งคนเป็นจำนวน {People} คนได้คนล่ะ {Flo}บาท")
print("เงิน",Money,"แบ่งคนเป็นจำนวน",People,"คนได้คนล่ะ",Flo,"บาท")
print(str("เงิน")+str(Money)+str("แบ่งคนเป็นจำนวน")+str(People)+str("คนได้คนล่ะ")+str(Flo)+str("บาท"))