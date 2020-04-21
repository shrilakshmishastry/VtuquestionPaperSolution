l = map(int,input("enter numbers").strip().split())
l = list(l)
count = 0
sum = 0
avg = 0
for i in l:
    count = count+1
    sum  = sum+i
print("count = %.d sum = %.d avg = %.2f"%(count,sum,(sum/count))    )
