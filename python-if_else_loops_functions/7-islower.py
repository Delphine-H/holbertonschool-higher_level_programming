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
