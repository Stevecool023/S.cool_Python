#!/bin/python3
# This program calculates the compound interest over a period of time.
# The principal amount is incremented by a constant every year.
# Formulae: Compound interest = k + (principal * (1 + interest_rate))

def main():
    print()
    print('This program calculates the compound interest', end=' ')
    print('through an inputed number of years using a loop.')
    print()

    principal = input("Enter the principal amount: ")
    rate = input("What is the annual interest rate? ")
    n = input("Enter the number of investment years: ")
    k = input("What is your additional savings per year? ")

    principal = float(principal)
    rate = float(rate)
    n = int(n)
    k = float(k)

    for i in range(n):
        principal = k + (principal * (1 + rate))

    print()
    print(f"Congrats! Your investment after", n, "years is", principal)
    print()

main()
