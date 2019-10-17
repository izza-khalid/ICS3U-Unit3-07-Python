#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: October 2019
# This program tells if you can date a grandchild of a grandmother
# with user input


def main():
    # This function tells if you can date a grandchild of a grandmother

    # input
    your_money = (input("Are you rich ($100,000+ salary)?: "))
    your_looks = (input("Do people consider you good-looking (naturally!)? "))

    # process & output
    if your_money == "yes" or your_looks == "yes":
        print("")
        # output
        print("You have been granted permission to date!")
    else:
        print("")
        print("You have been denied permission to date!")


if __name__ == "__main__":
    main()
