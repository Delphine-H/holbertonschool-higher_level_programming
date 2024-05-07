#!/usr/bin/python3
for firstDigit in range(0, 8):
    for secDigit in range(firstDigit + 1, 10):
        print("{:d}{:d}, ".format(firstDigit, secDigit), end="")
print("89")
