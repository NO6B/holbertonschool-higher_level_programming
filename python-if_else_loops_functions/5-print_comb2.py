#!/usr/bin/python3
i = 0
while i <= 99:
    if i < 10:
        print("0{}, ".format(i), end="")
    else:
        print("{}, ".format(i), end="")
    i+= 1
