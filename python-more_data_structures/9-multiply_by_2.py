#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic = a_dictionary.copy()
    for i in dic.keys():
        dic[i] *= 2
    return dic
