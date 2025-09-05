#!/usr/bin/python3
import sys
if __name__ == "__main__":

    arguments = sys.argv[1:]
    if len(arguments) == 1:
        argm = "argument"
    elif len(arguments) > 1:
        argm = "arguments"
    elif len(arguments) < 1:
        argm = "argument"

    print(f"{len(arguments)} {argm}:")
    
    for j, i in enumerate(arguments, start= 1):
        print(f"{j}: {i}")
