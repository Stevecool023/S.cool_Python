#!/bin/python3
# This progran converts temperature in Fahrenheit
# +to degrees celsius.
# Mathematical formulae: F = 9/5C + 32.

def main():
    print("convert degrees celsius to degrees fahrenheit")
    print()

    print("degrees_celsius", "degrees_Fahrenheit "
            "", sep='   ')
    
    for celsius in range(0, 100, 10):
        # conver celsius to F.
        F = 9 / 5 * celsius + 32

        print("{:<20} {:.2f}".format(celsius, F))
        print()
    
    print()

main()
