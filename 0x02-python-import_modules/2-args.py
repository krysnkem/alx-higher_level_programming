#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    num_args = len(argv) - 1
    args_text = ""
    if num_args == 1:
        args_text = "argument"
    else:
        args_text = "arguments"

    if num_args == 0:
        args_text = args_text + "."
    else:
        args_text = args_text + ":"

    print("{} {}".format(num_args, args_text))

    for index in range(1, num_args + 1):
        print("{}: {}".format(index, argv[index]))
