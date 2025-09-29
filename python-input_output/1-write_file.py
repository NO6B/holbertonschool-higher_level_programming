#!/usr/bin/python3
def write_file(filename="", text=""):
    count = 0
    with open(filename, mode="w", encoding="utf-8") as f:
        for i in text:
            f.write(i)
            count += 1
    return count
