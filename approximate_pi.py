#!/usr/bin/env python3

# Approximate the value of pi by summing the terms of this series:
# + Leibniz formula for pi: 4/1-4/3+4/5-4/7+4/9-4/11+...
# Prompt the user for number of terms to add.
# Output sum of first n terms of series.
# Subtract approximation from the value of math.pi to see accuracy.

import math
print()
print('Program to approximate the value of pi using Leibniz formula for pi')
total = 0
denominator = 1
n = int(input('Enter number of terms to add: '))
for i in range(n):
    term = 4/denominator
    if i%2 == 0:
        total += term
    else:
        total -= term
    denominator += 2
print(f'Approximation of pi using {n} terms: {total}')
print(f'Accuracy compared to math.pi: {abs(math.pi-total)}')

