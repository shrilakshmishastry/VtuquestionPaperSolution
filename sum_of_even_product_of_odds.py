n = map(int,input().strip().split())
n = list(n)
sum =0
product =1
for i in n:

    if (i%2==0):
        sum = sum+i
    else:
        product*=i
print("sum{},product{}".format(sum,product) )        
