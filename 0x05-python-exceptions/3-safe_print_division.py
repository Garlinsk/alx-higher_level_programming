#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print("Inside result: ", end='')
        total = a / b
    except ZeroDivisionError:
        total = None
    finally:
        print("{}".format(total))
    return total
