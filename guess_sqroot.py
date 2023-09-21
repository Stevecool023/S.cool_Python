#!/usr/bin/env python3

# This program implements the Newton's method: (guess + (x/guess)) / 2
# Prompt the user for the value to find the sqrtoot of (x) and the number of times to improve the guess.
# Start with a guess value of (x/2).

import math
print()
print("Approximate the squareroot of a number by implementing Newton's guess method.")
x = float(input('Enter the number x to approximate its squareroot: '))
n = int(input('number of times to improve guess: '))
guess = x/2
for i in range(n):
    guess = (guess + (x/guess)) / 2
print('The approximate squareroot of {} after {} improvements is: {}'.format(x, n, guess))
print('Variation from actual squareroot is: {}'.format(abs(math.sqrt(x)-guess)))
