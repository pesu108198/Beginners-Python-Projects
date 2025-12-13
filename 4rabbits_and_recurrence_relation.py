
def fib():
    a=1
    b= 1
    k = int(input("enter no. of offspring: "))
    n = int(input("enter the no. of months: "))

    print (a)
    print(b)

    for i in range(3, n+1):
        c = a + k*b
        b = a
        a = c
        
       
        print(c)

fib()