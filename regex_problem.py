##6b dec 2018
import re
ffrom = open("from.txt")
for  i in ffrom:
    # print(i)
    if (re.findall(".*@.*",i)):
        # print(i)
        pass
    if(re.findall("\S@\S",i))    :
        print(i)
