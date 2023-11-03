#!/usr/bin/python3
"""

Module composed by a function that prints 2 new lines after ".?:" characters

"""


def text_indentation(text):
    """ prints 2 new lines after ".?:" characters

    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        lll = s.split(d)
        s = ""
        for i in lll:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="")
