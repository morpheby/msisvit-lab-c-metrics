#!/usr/bin/env python3

""" Entry point for metrics app """


import sys, getopt, helper, code_cleanup, functioner, graph, holsted, myers, boundary

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
    
    print('\n')

    text = input_file.read()
    
    if use_metric == 'holsted':
        h = holsted.Holsted(text)
        h.run()
    elif use_metric == 'myers':
        text = code_cleanup.cleanup_strings(code_cleanup.cleanup_sharp(code_cleanup.cleanup_comments(text)))
        g = graph.ExecGraph(text)
        g.build_graph()
        m = myers.Myers(g, text)
        m.analyze()
        print('Метрика Майерса:', m.metric())
    elif use_metric == 'boundary':
        text = code_cleanup.cleanup_strings(code_cleanup.cleanup_sharp(code_cleanup.cleanup_comments(text)))
        g = graph.ExecGraph(text)
        g.build_graph()
        b = boundary.Boundary(g)
        b.analyze()
        print('Метрика Майерса:', b.metric())



#try:
main(sys.argv)
#except SyntaxError:
#    (_, text, _) = sys.exc_info()
#    print(text)
#except:
#    print('Syntax parsing error')
#    print(sys.exc_info())





# vim:tabstop=4:shiftwidth=4:expandtab

