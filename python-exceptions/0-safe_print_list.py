#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    print_element = 0
    for element in range(x):
        try:
            print("{}".format(my_list[element]), end="")
            print_element += 1
        except:
            break

    print()

    return print_element
