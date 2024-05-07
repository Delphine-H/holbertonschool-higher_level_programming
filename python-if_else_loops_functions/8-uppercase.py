#!/usr/bin/python3


def islower(c):
    """
    Check if a character is a lowercase letter.

    Args:
        c (str): The character to check.

    Returns:
        bool: True if the character is a lowercase letter, False otherwise.
    """
    if ord(c) >= ord("a") and ord(c) <= ord("z"):
        return True
    else:
        return False


def uppercase(str):
    """
    Convert all lowercase letters in a string to uppercase.

    Args:
        str (str): The input string.

    Returns:
        str: The input string with all lowercase letters converted to uppercase.
    """
    string = ""
    for char in str:
        if islower(char):
            string += chr(ord(char) - 32)
        else:
            string += char
    print(string)
