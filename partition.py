def partition(f, liste):
    #searching 2 times in the list this is problem
    return [[x for x in liste if f(x)], [y for y in liste if not f(y)]]



print partition(lambda x: x>3, [2.4, 1.3, 1.5, 4.6, 4.3, 4.4])
