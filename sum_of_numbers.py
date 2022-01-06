#!/usr/bin/env python3

# Created by: Ketia Gaelle Kaze
# Created on: Jan. 5, 2022
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display the sum
# of all numbers from 0 to the number the user entered.

def main():
    # initialize the loop counter and sum
    loop_counter = 0
    sum = 0

    # get the user number as a string
    user_number_string = input("Enter a positive number: ")
    print("")
    # checks to catch errors
    try:
        # changes user number as string to an integer
        user_number = int(user_number_string)
        # checks to see if user number is an positive number
        if (user_number > 0):
            # calculate the sum of all numbers from 0 to user number
            while (loop_counter <= user_number):
                sum = sum + loop_counter
                print("Tracking {0} times through loop.".format(loop_counter))
                loop_counter = loop_counter + 1

            print("")
            print("The sum of the numbers from 0 to {} is: {}."
                  .format(user_number, sum))
        else:
            print("{} is not a positive number.".format(user_number_string))
    except Exception:
        print("{} is not a number.".format(user_number_string))


if __name__ == "__main__":
    main()
