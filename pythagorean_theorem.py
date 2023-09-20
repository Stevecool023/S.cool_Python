#!/usr/bin/env python3

# This program accepts two points
# + and determines the distance between them.
# Pythagorean theorem: c^2 = b^2 + a^2.
# distance = sqrt((x2-x1)^2 + (y2-y1)^2)

import math     # In order to use the squareroot function.
print()
print('This program calculates distance between two points '
        'on a cartesian plane')

x1 = float(input("Enter point_1 x1: "))
y1 = float(input("Enter point_1 y1: "))
x2 = float(input("Enter point_2 x2: "))
y2 = float(input("Enter point_2 y2: "))

ab = (x2-x1)*2 + (y2-y1)*2
distance = math.sqrt(ab)
print("Distance between this two points is {}.".format(distance))
print()
