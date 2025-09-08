#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    origin_list = my_list[0:]
    if idx < 0 or idx >= len(my_list):
        return origin_list
    origin_list[idx] = element
    return origin_list
