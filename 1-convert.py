#!/bin/python3
# This progran converts temperature in Fahrenheit
# +to degrees celsius.
# Mathematical formulae: F = 9/5C + 32.

def main():
    print("convert degrees celsius to degrees fahrenheit")
    
    for i in range(5):
    # Prompt user to input temp value in C.
        celsius = eval(input("Enter temp in degrees celsius: "))
    # conver celsius to F.
        F = 9 / 5 * celsius + 32
    
        print("{} degrees celsius equals "
        "{:.2f} degrees Fahrenheit".format(celsius, F))

main()
