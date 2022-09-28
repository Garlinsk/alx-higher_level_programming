#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dic = a_dictionary
    [print("%s: %s" % (k, a_dic[k])) for k in sorted(a_dic.keys())]
