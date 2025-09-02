#!/usr/bin/python3
i = 0
while i <= 99:
    if i < 10:
        print("0{}, ".format(i), end="")
    elif i < 99:
        print("{}, ".format(i), end="")
    elif i == 99:
        print("{}".format(i))
    i+= 1
