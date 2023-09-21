#!/usr/bin/env python3

# This Program calculates the area of a triangle
# + given the length of its three sides; a, b and c.
# Formulas: s = (a+b+c)/2
#           Area = squareroot(S(s-a)(s-b)(s-c))

print()
print('Calculate area of a triangle given length of its three sides')
a = float(input("Enter length of side a: "))
b = float(input('Enter length of side b: '))
c = float(input('Einter lengty of side c: '))

s = (a+b+c) / 2
A = (s*(s-a)*(s-b)*(s-c))**.5
print('Area of triangle is {} square units.'.format(A))
print()
