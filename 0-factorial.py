#!/usr/bin/env python3

# This program calculates the factorial of a number.

def main():
    print()
    print("Evaluate the factorial of number n")
    print()

    n = int(input("Enter whole number n: "))
    arr = 1
    for i in range(n, 1, -1):
        arr = arr * i
    print(arr)
    print()

main()
