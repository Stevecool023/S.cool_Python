#!/usr/bin/env python3

# This program calculates the slope of a line
# + through two (non-vertical) points entered by the user.
# points (x1, y1) and (x2, y2).
# slope = (y2-y1) / (x2-x1).

print()
print("Calculating the slope of a line.")

x1 = float(input("Enter point_1 x1: "))
y1 = float(input("Enter point_1 y1: "))
x2 = float(input("Enter point_2 x2: "))
y2 = float(input("Enter point_2 y2: "))

slope = (y2-y1) / (x2-x1)
print(f"The slope/gradient of this line is {slope}")
print()
