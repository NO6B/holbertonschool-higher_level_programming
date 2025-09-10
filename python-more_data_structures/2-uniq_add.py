#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] not in new_list:
            new_list.append(my_list[i])
    result = 0
    for i in new_list:
        result += i
    return result
