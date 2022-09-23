#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_list.append(1)
        else:
            new_list.append(0)
    return new_list
