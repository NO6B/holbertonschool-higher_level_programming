#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argm = sys.argv[1:]
    result = 0
    for i in argm:
        result += int(i)
    print(result)
