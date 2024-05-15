#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    print_element = 0
    try:
        for element in range(x):
            print("{}".format(my_list[element]), end="")
            print_element += 1
        print()
        return print_element
    except:
        print()
        return print_element
