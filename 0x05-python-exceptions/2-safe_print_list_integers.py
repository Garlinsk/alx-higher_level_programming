#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

"""
    i = 0
    sum = 0
    while x > i:
        try:
            print("{:d}".format(my_list[i]), end='')
            sum += 1
            i += 1
        except(ValueError, TypeError):
            i += 1
    print("")
    return sum"""

    index = printed_ints = 0
    while True:
        try:
            if index < x:
                print("{:d}".format(my_list[index]), end='')
                index += 1
                printed_ints += 1
            else:
                print()
                return printed_ints
        except (ValueError, TypeError):
            index += 1
