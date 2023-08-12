#!/bin/python3
# This program illustrates chaotic behavior.
# It is inspired by the form: k(x)(x-1)
# + and is widely employed by physicists and in the field of mathematics.
# This concept can be applied in weather patterns prediction.
# + #//the butterfly effect.

def main():
    print('A simple program illustrating chaotic behavior')
    x = eval(input('Enter a number between 0 and 1: '))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)

main()
