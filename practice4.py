# fizzbuzz problem:
# build a function that takes in 'n' (does not return anything) and does the following 
# generate numbers 0 to n (inclusive)
# print each number unless one the bottom 3 expression are true. print each number when the bottom three are NOT true.
# and if a number is divisible by 2 and not 3, print "fizz"
# and if the number is divisible by 3 and not 2 print "buzz" 
# and if the number is divisible by 2 and 3 print "fizzbuzz"

def fizzbuzz(n):
    i = 0
    while(i <= n):
        if i % 2 == 0 and i % 3 != 0:
            print('fizz')
        elif i % 3 == 0 and i % 2 != 0:
            print('buzz')
        elif i % 2 == 0 and i % 3 == 0:
            print('fizzbuzz')
        else: 
            print(i)
        i = i + 1

fizzbuzz(10)