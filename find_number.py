import re

fopen = open("from.txt")
num = []
for i in fopen:
    x = re.findall("^X\S*:[0-9]+",i)
    if(len(x)>0):
        print(int(x[0].split(":")[1]))
        num.append(int(x[0].split(":")[1]))
print(sum(num)        )
