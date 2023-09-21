#!/usr/bin/env python3

# Find average of series of  numbers entered by the user.
# First prompt the user for how many numbers are to be averaged.
# Prompt the user for each of the numbers in turn.
# Print out the average after all the numbers have been entered.

print()
print('Average of series of numbers entered by the user.')
n = int(input('Enter count of numbers to be averaged: '))
total = 0
for i in range(n):
    i = float(input(f'{i+1} : '))
    total = total + i
    a = total / n
print('Average of the above', n, 'numbers is ', a)
print()
