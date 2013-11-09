#!/usr/bin/env python3

""" Entry point for metrics app """


import sys, getopt

def usage():
    """ Outputs usage info """
    print("Usage: ", sys.argv[0], " -m [myers|boundary|holsted] inputfile")
    sys.exit(2)

def main(argv):
    """ Entry point method """
    try:
        opts, args = getopt.getopt(argv[1:], "m:", ["metric="])
    except getopt.GetoptError:
        usage()
    
    for opt, arg in opts:
        if opt in ["-m", "--metric"]:
            use_metric = arg
        else:
            usage()
    
    if len(args) != 1:
        usage()
    elif args[0] == '-':
        input_file = sys.stdin
    else:
        input_file = open(args[0], 'r')
    print(input_file)
    print(use_metric)

main(sys.argv)



# vim:tabstop=4:shiftwidth=4:expandtab

