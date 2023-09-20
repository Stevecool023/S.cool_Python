#!/usr/bin/env python3

# This program computes the molecular weight of a carbohydrate.
# The computation is in grams per mole.
# Based on the number of hydrogen, carbon and oxygen atoms.
# Print the total combined molecular weight of all the atoms
# + based on the individual atom weights.

        
#       Atom    Weight(grams/mole)
#       H       1.00794
#       C       12.0107
#       O       15.9994

# Example: molecular weight of water(H20) is;
# 2(1.00794) + 15.9994 = 18.01528

H = 1.00794
C = 12.0107
O = 15.9994

print()
print('Compute the molecular weight of a carbohydrate')
print('Entr "0" if an atom is absent')
Hydrogen = int(input("Number of hydrogen atoms: "))
Carbon = int(input("Number of Carbon atoms: "))
Oxygen = int(input("Number of Oxygen atoms: "))

Weight = H*Hydrogen + C*Carbon + O*Oxygen

print("Molecular weight of carbohydrate is", Weight, "grams/mole")
print()
