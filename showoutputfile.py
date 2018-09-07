import ast, sys, pprint
pprint.pprint(ast.literal_eval(open(sys.argv[1]).read()))
