#เขียนข้อมูลลงไฟล์
f_dti = open('myfile02.txt','w',encoding='utf-8') #เปิดไฟล์เพื่อเขียนข้อมูลลงไฟล์

f_dti.write('SAU......')
f_dti.write('DTI.......\n')
f_dti.write('Bye.....\n')

f_dti.close()

print("บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว...")