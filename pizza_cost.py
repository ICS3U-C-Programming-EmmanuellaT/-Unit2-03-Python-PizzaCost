#!/usr/bin/env python3
# Created By: Emmanuella Taiwo
# created on 25th Sep, 2026
# This program asks the user for the diameter of the
# Pizza. It then calculates and displays the cost
# of the pizza.
import constants


def main():
    # input
    diameter = int(input("Enter the diameter of the pizza (inches): "))

    # process
    subtotal = constants.LABOUR_COST + constants.RENTAL_COST 
    + constants.INGRED_COST * diameter
    tax = constants.HST * subtotal
    total = subtotal + tax

    # output
    print("")
    print("The total cost is: ${:.2f}".format(total))


if __name__ == "__main__":
    main()
