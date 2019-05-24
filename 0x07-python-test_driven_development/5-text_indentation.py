#!/usr/bin/python3

def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    n = 0
    for a in text:
        if n == 0:
            if a == ' ':
                continue
            else:
                n = 1
        if n == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                n = 0
            else:
                print(a, end="")
