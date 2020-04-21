import re

st= input("enter a password\n")
st = list(st)
d= dict()
d["LETTERS"] =0
d["DIGITS"]=0
d["UPPER CASE"] =0
d["LOWER CASE"] = 0
d["SPECIAL CASE"]=0
for i in st:
    d["LETTERS"]=d["LETTERS"]+1

    if(re.search("[a-z]",i)):
        d["LOWER CASE"] = d["LOWER CASE"]+1

    if(re.search("[A-Z]",i)) :
        d["UPPER CASE"]   = d["UPPER CASE"]+1

    if(re.search("[1-9]",i))    :
        d["DIGITS"]  =d["DIGITS"]+1

    if(re.search("[$#@!]",i))    :
        d["SPECIAL CASE"] = d["SPECIAL CASE"]+1
print(d)

if(d["LETTERS"] >=6 and d["UPPER CASE"] > 0 and d["LOWER CASE"]>0 and d["DIGITS"]>0 and d["SPECIAL CASE"]>0):
    print("valid")
else:
    print("invalid")
