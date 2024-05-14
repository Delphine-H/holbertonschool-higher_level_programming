#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    new_list = []
    for nbr in my_list:
        new_list.append(nbr % 2 == 0)
    return new_list
