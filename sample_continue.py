n = int(input("enter the limit of natural numbers"))
sum =0
for i in range(0,n):
    if(i%2!=0):

        continue
    if(i == 100)    :
        break
    sum= sum+i
print(sum)
