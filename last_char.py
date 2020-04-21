import re
# jun 2018 4b
str = "Make hay while the sun shines"
print(str[len(str)-7:])
#jun 2018
fname = input("enter a file name\n")
n = int(input("enter the number of lines\n"))
word = input("enter the word to be find\n")
try:
    fline = open(fname)
    count = 0
    frequency = 0
    for  i in fline:

        if count>n:
            break
        # print(type(i))
        if (len(re.findall(word,i))):
            frequency = frequency+len(re.findall(word,i))
        count = count+1
    print(frequency)
except Exception as e:
    print(e)
