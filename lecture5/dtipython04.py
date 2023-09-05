def dti1(c,d) : 
    print(f"{c}ยกกำลัง{d} = {c ** d}")
    return c ** d

def dti2 (c,d,e,f) :
    return c+d+e+f+dti1(2,3) , "W"

x,y = dti2(4,8,12,16)

print(f"{x} Bro {y}")