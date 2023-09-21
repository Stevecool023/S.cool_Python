#!/usr/bin/env python3

# Calculate the sum of the first n natural numbers.
# n is provided by the user.

print()
print('Calculating the sum of the first n natural numbers.')
total = 0
n = int(input('Enter number of natural numbers: '))
for i in range(n+1):
    total = total + i
print(f'Sum of the first {n} natural numbers is {total}')
print()
