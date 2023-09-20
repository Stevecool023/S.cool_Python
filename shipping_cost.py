#!/usr/bin/env python3

# This program calculates the cost of an order.
# Coffee shop sells coffee at $10.50 a pound.
# There is additional cost of shipping.
# Each order ships for $0.86 per pound + $1.50 fixed cost for overhead

print()
print("Calculate cost of an order or identical orders.")
orders = int(input("Enter number of orders: "))
pounds = float(input("Enter weight of coffee in pounds: "))
shipping = 0.86
overhead = 1.50
coffee = 10.50
Cost = ((shipping + coffee) * pounds) + 1.50
Total_cost = Cost * orders

print("The cost of this order(s) is $ {}".format(Total_cost))
print()
