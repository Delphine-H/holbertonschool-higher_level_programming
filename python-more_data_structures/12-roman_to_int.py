#!/usr/bin/python3


def roman_to_int(roman_string):
    if (type(roman_string) is not str) or (roman_string is None):
        return 0

    roman_numeral = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    previous = 0

    for nbr in roman_string[::-1]:
        current = roman_numeral[nbr]
        if previous > current:
            result -= current
        else:
            result += current
        previous = current

    return result
