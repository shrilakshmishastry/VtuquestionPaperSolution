#2018 jun 1c
m1,m2,m3 = input("enter marks\n").strip().split()
print(m1,m2,m3)
m1 = int(m1)
m2 = int(m2)
m3 = int(m3)
if(m1>=m2 and m1>=m3):
    if(m2>m3)    :
        avg = m1+m2
    else:
        avg = m1+m3
elif(m2>=m3 and m2>=m1)            :
    if(m3>m1):
        avg = m2+m3
    else:
        avg = m2+m1
elif(m3>=m1 and m3>=m2)            :
    if(m1>m2):
        avg = m3+m1
    else:
        avg = m3+m2
print(avg)
