#!/bin/python3
# A simple program that returns the average of two exam scores.
# Also illustrates use of multiple input.

def main():
    print ("This program computes the average of two exam scores. ")
    score1, score2 = eval(input("Enter two scores separated by a comma: "))
    average = (score1 + score2) / 2
    print("The average of the scores is: ", average)

main()
