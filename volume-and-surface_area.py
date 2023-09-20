#!/usr/bin/env python3

# Calculate the volume and surfave area of a sphere from its radius.
# The radius is given as input.
# Prompt the user to input units of the radirs, i.e., cm, metres
# V = 4/3(pi)r^3
# A = 4(pi)r^2

import math # In order to use pi.
print()
r = float(input("Please enter the radius of float data type: "))
units = str(input("What are the units of your radius? "))
Volume = (4/3) * math.pi * (r**3)
Area = 4 * math.pi * (r**2)
print("Volume = ", Volume, "cubic", units)
print("Area = ", Area, "square", units)
print()
