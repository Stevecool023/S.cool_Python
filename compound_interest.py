#!/bin/python3
# This program calculates the compound interest of an investment
# + after 10 years using a loop.
# It applies the relationship:
# + "value for one year = principal(1 + interest_rate)".

def main():
    print('This program calculates the compound interest', end=' ')
    print('after 10 years using a loop.')
    principal = eval(input("Enter the principal amount: "))
    rate = eval(input("What is the annual interest rate? "))

    for i in range(10):
        principal = principal * (1 + rate)
    print("The total amount after 10 yrs is: ", principal)

main()
