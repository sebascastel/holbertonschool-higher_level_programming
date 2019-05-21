#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    variables used:
    my_list : can hold any type of element
    x : number of elements to be printed
    return number of elements printed
    """
    elements = 0
    while elements < x:
        try:
            print("{}".format(my_list[elements]), end="")
            elements += 1
        except IndexError:
            break
    print()
    return elements
