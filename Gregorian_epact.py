#!/usr/bin/env python3

# Prompt the user for a 4-digit year and then output the value of the epact
# Gregorian epact is the number of days between 
# + January 1st and the previous new moon.
# This value is used to figure out the date of Easter.
# It's calculated using int arithmetic.
# Formulaes:    C = year//100
#           epact = (8 + (C//4) - C + ((8C+13)//25) + 11(year%19))%30

print()
print("Evaluate the value of the epact")
year = int(input("Enter 4-DIGIT year: "))
C = year//100
epact = (8 + (C//4)- C + ((80 + 13)//25) + 11*(year%19))%30
print('The number of days by which the solar year exceeds the lunar year '
        'in', year, 'are', epact)
print()
