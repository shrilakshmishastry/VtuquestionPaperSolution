import re
try:
    fhand = open("from.txt")
    print(fhand)
    fout = open("vowel.txt","w")
    for i in fhand:
        print(i)
        if re.search("^[aeiouAEIOU][a-zA-Z]*",i):
            print("hello")
            print(i)
            fout.write(i)


except Exception as e:
    print(e)
