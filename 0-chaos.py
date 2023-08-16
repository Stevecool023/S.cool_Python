#!/bin/python3
# Illuatrating the chaotic behavior.
# The user should be prompted to input:
# +the number of lines to print,
# + a number to be manipulated and a constant.

def main():
    print('program illustrating chaotic behavior.')
    n = eval(input('How many lines should I print? '))
    x = eval(input('Enter a number between 0 and 1: '))
    k = eval(input("What constant should I use? "))
    for i in range (n):
        x = k * x * (1 - x)
        print(x)
main()
