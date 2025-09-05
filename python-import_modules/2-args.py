#!/usr/bin/python3
import sys

if __name__ == "__main__":



    arguments = (sys.argv)
    argv = len(arguments)-1

    if argv == 0:
        print("0 arguments.")
    elif argv == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argv))

    for i in range(argv):
        print("{}: {}".format(i + 1, arguments[i + 1]))