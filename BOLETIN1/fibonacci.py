
def fibo (num):
 if num < 1:
   print(num)
 else :
    val1 = 0
    val2 = 1
    for i in range(num):
        temp = val1
        val1 = val2
        val2 = temp + val1
    print(val2)
