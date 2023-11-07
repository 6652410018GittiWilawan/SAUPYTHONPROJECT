#ลบไฟล์
import os 
from os import remove
if os.path.exist("myfile02.txt") :
    # os.remove("myfile01.txt")
    remove("myfile01.txt")
    print("ลบไฟล์เรียบร้อยเเล้ว")
else :
    print("ไฟล์ที่จะลบ")