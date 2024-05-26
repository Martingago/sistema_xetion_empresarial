def factorial(num) :
    if num < 1:
        print(num)
    else:
        acum = 1
        for i in range(num) :
            acum = acum * (i+1)
        print(acum)
