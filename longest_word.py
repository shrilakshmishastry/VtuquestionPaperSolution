string =map(str,input("enter a string\n").strip().split())
# print(list(string))
# string1 = list(string)
prev = 0
# print(string1)
for i in list(string):
    print(i)
    maxlen = len(i)
    print(maxlen)
    if(maxlen>prev):
        word = i
        prev = maxlen
print(prev,word)
