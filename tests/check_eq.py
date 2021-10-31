def checkEq(f1, f2):
    f1 = open(f1, 'r')
    f2 = open(f2, 'r')
    return f1.read() == f2.read()
