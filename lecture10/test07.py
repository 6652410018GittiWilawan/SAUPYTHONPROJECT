f_dti = open('myfile01.txt','r',encoding='utf-8')

try:
    data = f_dti.read() 
    
    for data_by_line in data :
        print(data_by_line=" ")
    
except Exception :
    print("ติดต่อ Admin 02******** ")
finally :
    f_dti.close ()