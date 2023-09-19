#!/bin/python3

# Calculating the real roots of a quadratic
# Use exponentiation and not the math library
# Quadratic based on the formulae; x = -b (+/-) sqrt(b**2 - 4ac)

def main():
    print()
    print("Evaluate the real roots of a quadratic equation")

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    # sqrt(b**2 - 4ac) == (b**2 - 4ac)**(1/2)
    discriminantRoot = (b*b - 4*a*c) ** 0.5
    root1 = (-b + discriminantRoot) / (2*a)
    root2 = (-b - discriminantRoot) / (2*a)
    
    print("Quadratic roots are:", root1, root2)
    print()

main()
