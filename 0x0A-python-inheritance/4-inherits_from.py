#!/usr/bin/python3
""" Inherits_from  """


def inherits_from(obj, a_class):
    if type(obj) is a_class:
        return False
    else:
        return(isinstance(obj, a_class))
