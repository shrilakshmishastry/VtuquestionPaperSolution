def Solve(n,m):
    try:
        q = n//m
        r = n%m
        print("quotient",q)
        print("reminder",r)
    except Exception as e:
        print(e)
n = int(input("enter neumarator"))
m = int(input("enter denominator"))

Solve(n,m)
