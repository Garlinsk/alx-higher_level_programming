#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dic = {}
    for key, value in a_dictionary.items():
        b_dic[key] = (value * 2)
    return b_dic
