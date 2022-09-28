#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    remove = []
    for k, v in a_dictionary.items():
        if v == value:
            remove.append(k)
    for i in remove:
        del a_dictionary[i]
    return a_dictionary
