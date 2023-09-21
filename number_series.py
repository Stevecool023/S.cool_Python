#!/usr/bin/env python3

# Sum a series of  numbers entered by the user.
# First prompt the user for how many numbers are to be summed.
# Prompt the user for each of the numbers in turn.
# Print out the total sum after all the numbers have been entered.

print()
print('Sum of series of numbers entered by the user.')
n = int(input('Enter count of numbers to be summed: '))
total = 0
for i in range(n):
    i = float(input(f'{i+1} : '))
    total = total + i
print('Sum of the above', n, 'numbers is ', total)
print()
