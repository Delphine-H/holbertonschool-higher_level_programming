#!/usr/bin/python3


def uniq_add(my_list=[]):
    unique = set()
    for nbr in my_list:
        unique.add(nbr)
    return sum(unique)
