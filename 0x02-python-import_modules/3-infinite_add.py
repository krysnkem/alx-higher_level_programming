#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    result = 0
    for index in range(1, len(argv)):
        result = result + int(argv[index])

    print("{}".format(result))
