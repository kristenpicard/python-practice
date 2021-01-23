# 0 1 1 2 3 5 8 13 ... 
# x[n] = x[n-1] + x[n-2]
# function takes in n, doesn't return anyting, and prints out the fibonnaci series up to the nth number
# test your function by calling it with n = 10

def fib(n):
    i = 0
    xn2 = 0
    xn1 = 1
    xn = 1
    while(i<=n):
        if i == 0:
            print('0')
        elif i == 1:
            print('1')
        else:
            xn = xn1 + xn2
            print(xn)
            xn2 = xn1
            xn1 = xn


        i=i+1

fib(10)