#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = list.copy(my_list)
    if idx >= 0:
        for i in range(len(new_list)):
            if i == idx:
                new_list[i] = element
                return new_list
    return my_list
