#Written by Luke Pitstick

import sys;

#primaity test for prime
def isPrime(num):
    if(num == 1): return False
    elif(num <= 3): return True
    if(num % 2 == 0 or num % 3 == 0): return False
    j = 5
    while(j*j <= num):
        if(num % j == 0 or num % (j+2) == 0):
            return False
        j = j + 6
    return True

def fizzBuzzFib(n):
    fib = []
    fib.append(1)
    fib.append(1)
    
    #generate Fibonacci sequence
    for i in range(2,n):
        fib.append(fib[i-1] + fib[i-2])

    #print based on Fibonacci
    for i in range(n):
        if(isPrime(fib[i])):
            print("BuzzFizz")
        elif(fib[i] % 15 == 0):
            print("FizzBuzz")
        elif(fib[i] % 5 == 0):
            print("Fizz")
        elif(fib[i] % 3 == 0):
            print("Buzz")
        else:
            print(fib[i])

#run with first argument as n, or 55 as default
if(__name__ == "__main__"):
    try:
        fizzBuzzFib(int(sys.argv[1]))
    except IndexError:
        fizzBuzzFib(55)