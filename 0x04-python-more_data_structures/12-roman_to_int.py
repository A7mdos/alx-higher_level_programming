#!/usr/bin/python3

def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        values = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        ss = dict(I='VX', X='LC', C='DM')
        total = 0
        i = 0

        while i < len(roman_string):
            c = roman_string[i]
            if c in ss.keys():
                if i + 1 < len(roman_string) and roman_string[i + 1] in ss[c]:
                    total += values[roman_string[i + 1]] - values[c]
                    i += 1
                else:
                    total += values[c]

            else:
                total += values[c]
            i += 1
        return total

    else:
        return 0
