
# mod operator finds the remainder after division, the operator is %
g = 190 % 5

# fizzbuzz problem:
# loop through numbers 0 to N (inclusive) 
# print each number unless one the bottom 3 expression are true. print each number when the bottom three are NOT true.
# and if a number is divisible by 2 and not 3, print "fizz"
# and if the number is divisible by 3 and not 2 print "buzz" 
# and if the number is divisible by 2 and 3 print "fizzbuzz"



def fizzbuzz(n):
    # for integers in 0-n
    for i in range(0,n+1):
        # if integer is divisible by 2 and not 3, print "fizz"
        if i % 2 == 0 and i % 3 != 0:
            print("fizz")
        # if iteger is divisible by 3 and not 2, print "buzz"
        elif i % 3 == 0 and i % 2 != 0:
            print("buzz")
        # if integer is divisible by 2 AND 3, print "fizzbuzz"
        elif i % 2 == 0 and i % 3 == 0:
            print("fizzbuzz")
        # else print the integer
        else: 
            print(i)


fizzbuzz(1000)
