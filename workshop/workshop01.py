def inputnameprice():
    pricename = input("ป้อนชื่อสินค้า :")
    return pricename

def inputprice():
    price = float(input("ป้อนราคาสินค้า :"))
    return price

def inputCalprice(pricename,price):
    All = price + (price *10/100)
    print (f"ชื่อสินค้า{pricename}ต้นทุน{price}บาท ได้ราคา{All}บาท")

princename = inputnameprice()
price = inputprice()
print("------------------------------------")
inputCalprice(princename,price)
print("------------------------------------")