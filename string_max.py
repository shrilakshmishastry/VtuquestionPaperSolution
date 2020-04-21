import re
def string_max(Str):
    Str = list(Str)
    max = 0
    min = 99999
    count = 0
    for i in Str:
        count = count+1
        if(re.search(" ",i)):
            continue


        if(ord(i)>max):
            max = ord(i)
        elif(ord(i)<min)    :
            min = ord(i)
    print("maximum letter:",chr(max))
    print("minimum letter :",chr(min))
    print("length of string %.d"%count)

str = input("Enter a string")
for i in str:
    print(i,end= " ")
string_max(str)
