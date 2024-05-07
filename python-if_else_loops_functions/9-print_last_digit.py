#!/usr/bin/python3


def print_last_digit(number):
    """
    Print the last digit of a number.

    Args:
        number (int): The number whose last digit to print.

    Returns:
        int: The last digit of the input number.
    """
    lastDigit = abs(number) % 10
    print("{:d}".format(lastDigit), end="")
    return lastDigit
