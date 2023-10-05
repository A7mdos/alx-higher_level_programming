#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    argc = len(argv)
    arguments = argc - 1
    if arguments == 0:
        print("0 arguments.")
    elif arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arguments))

    for i in range(1, argc):
        print("{}: {}".format(i, argv[i]))
