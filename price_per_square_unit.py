#!/usr/bin/env python3

# This program calculates the cost per square inch of a circular pizza
# The pizza's diameter and price are inputed interactively.
# Calculation is based on the formulae: A = πr²
# Also: 1 inch == 2.54 cm == 0.0254 metres
# Or: 39.3701 == 1 metre == 100 centimetres
# Cost per square inch = Total cost / number of square inches.

import math # in order to use the math module.
print()
Cost = float(input("Input the cost of pizza: "))
r = float(input("Enter radius: "))
units = str(input("Enter radius units(cm, m, inch): "))

if units == "cm" or units == "centimetres":
    r = r/2.54
elif units == "m" or units == "metres":
    r = r/.0254
elif units == "inch" or units == "inches":
    r = r
else:
    print("Please enter radius of units: inch/inches, cm/centimetres "
    "m/metres")

Area = math.pi * r**2
inch_cost = Cost / Area

print("The cost per square inch of this pizza is: ", inch_cost)
print()
