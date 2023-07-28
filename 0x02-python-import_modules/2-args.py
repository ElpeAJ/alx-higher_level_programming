#!/usr/bin/python3

def args(argv):
    i = 0
    s_argv = argv.split(" ")
    print(type(s_argv))
    for i in len(s_argv):
        if i == 0:
            print(".")
        elif i !=0:
            i += 1
        print("{} arguments:\n".format(i))
        print("{}: {}\n".format(i, s_argv[i]))
