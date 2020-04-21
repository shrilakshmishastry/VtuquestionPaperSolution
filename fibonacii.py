def fibonacci(n):
    if n<=0:
        print( "Please enter valid")
    elif n==1:
        print(0)
    else:

        prev = 1
        prePrev =0
        print(prePrev)
        print(prev)
        for i in range(2,n)        :
            fn = prev+prePrev
            print(fn)
            prePrev=prev
            prev = fn
i = int(input("How many terms need to be generated?"))
fibonacci(i)
