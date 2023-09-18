#!/bin/python3

def main():
    print()
    print('Change Counter')
    print()
    print("please enter the count of each coin")
    quarters = eval(input("Quarters: "))
    dimes = eval(input("Dimes: "))
    nickels = eval(input("Nickels: "))
    pennies = eval(input("Pennies: "))
    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
    print("The total value of you change is", total)

main()
