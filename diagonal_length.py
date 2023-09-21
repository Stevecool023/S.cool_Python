#!/usr/bin/env python3

# Determine the length of ladder required to reach a certain length when leaned against a wall.
# Height and angle of ladder are given as input.
# Length = height / (sin angle)
# Angle must be in radians. Prompt angle in degrees then convert it to radians.
# radians = (pi/180) * degrees.

import math
print()
print('Calculate the length of a ladder using height and angle')
h = float(input('Enter height of wall: '))
a = float(input('Enter angle of ladder in degrees: '))
radians = (math.pi / 180) * a
L = h / (math.sin(a))
print('Length of ladder required for this wall is {} units.'.format(L))
print()
