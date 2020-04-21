import re
str1 = open("from.txt")

for i in str1:
    

    if(re.search("^F..m:*",i)):

        print(i)
