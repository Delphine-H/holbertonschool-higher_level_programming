#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for nbr in my_list:
            if nbr > max:
                max = nbr
        return max
    return None
