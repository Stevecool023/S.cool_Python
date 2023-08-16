#!/bin/python3
# illustrating chaotic behavior.
# Prompt user to input two numbers, a constant
# + and desired number of outputs.
# The output is a comparison of two columns.

def main():
    print("Illustrating chaotic behavior")
    n = eval(input("How many lines should I print? "))
    k = eval(input("Input desired constant: "))
    numbers = input("Enter two numbers between 0 and 1 "
            "seperated by a space character: ")
    x, y = numbers.split()
    x = float(x)
    y = float(y)

    if 0 <= x <= 1 and 0 <= y <= 1:
        print('x = {:<20} y = {}'.format(x, y))
        for i in range (n):
            x = k * x - k * x * x
            y = k * y - k * y * y
            print('{:<20} {:>20}'.format(x, y))
    else:
        print("Please input two numbers between 0 and 1 "
                "seperated by space")

main()
