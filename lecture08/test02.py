#list
my_list = [10,20,30,'Yo',True,[20,"Wass"],(10,20),{"SAU","DTI"}]

#Tuple 
my_tuple = (10,20,30,'Yo',True,(20,"Wass"),{10,20},{"SAU","DTI"})
print()#อยากเเสดงDTI

#Set ไม่มีลำดับ
my_set = {10,20,10,'Yo',True}

            # Key:คือ assoiative คือตัวชี้ที่่อ้างอิงไปยัง Value 
            # Value: คือคค่าข้อมูลที่สามารถเอาไปใช้งาน
#Dictionary -> Key:Value / key->String-Number / Value-> Everthing 
my_dict = {'name':'สมโบ','age':20, 500:900,'flag':True}

print(my_dict['name'])
print(my_dict['age']+my_dict[500])
my_dict['name'] = 'สมโบ'
print (my_dict)
my_dict.pop('name')
my_dict.pop(500)
print(my_dict)
my_dict.popitem()
print (my_dict)


for data in my_dict :
    print(data,end='')

print()

for data in my_dict.keys():
    print(data,end='')

print()

for data in my_dict.values():
    print(data,end='')

print()

my_dict1 = {'a':10,'b':20,'c':30}

my_dict2 = my_dict1

my_dict3 = my_dict1.copy()

print()
print(my_dict2)
print(my_dict3)
my_dict1['a'] = 700
my_dict3['a'] = 888
print("-------------------------")
print (my_dict1)
print (my_dict2)
print (my_dict3)

x=20
y=x