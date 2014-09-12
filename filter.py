def myfilter(function, liste):
    return [x for x in liste if function(x)]

print myfilter(lambda x: x > 10, [3, 7, 2, 546, 23, 42, 23])
