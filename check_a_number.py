i = input()
try:
    i = int(i)
    if(i==0):
        print("zero")
    elif (i<0):
        print("Negitive")
    else:
        print("Positive")
except Exception as e:
    print(e)
