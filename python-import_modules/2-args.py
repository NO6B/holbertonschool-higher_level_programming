#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    argm = len(arguments)

    if argm == 0:
        print("0 arguments.")
    elif argm == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argm))

    for i, j in enumerate(arguments, start=1):
        print("{}: {}".format(i, j))