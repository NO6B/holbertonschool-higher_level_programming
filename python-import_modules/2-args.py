#!/usr/bin/python3
import sys

if __name__ == "__main__":

    argument = len(sys.argv) -1

    if argument == 0:
        print("0 arguments.")
    elif argument == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argument))

    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
