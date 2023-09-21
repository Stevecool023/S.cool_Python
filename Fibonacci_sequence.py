#!/usr/bin/env python3

# Compute the nth fibonacci number where n is a value input by the user.
# The Fibonacci sequence is a sequence of numbers where each successive number is the sum or the previous two numbers.
# Classic Fibonacci sequence begins: 1,1,2,3,5,8,...

print()
print('Compute the nth Fibonacci number')
n = int(input('Enter value of n for nth fibonacci calculation: '))

# Initialize the first two numbers in the fibonacci series.
fib_prev = 1
fib_current = 1

# Check if n is 1 or 2 in order to handle the first two cases seperately.
if n == 1:
    result = 1
elif n == 2:
    result = 1
else:
    # Calculate the nth fibonacci number using a for loop.
    for i in range(3, n+1):
        fib_next = fib_prev + fib_current
        fib_prev = fib_current
        fib_current = fib_next
    result = fib_current
    # Display the result.
print(f'The {n}th number in the fibonacci series is: {result}')
