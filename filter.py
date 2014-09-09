l = [1, 23, 4, 5, 3, 5, 2, 5, 223, 423]


def my_filter(fun, liste):
    for i in liste:
        if fun(i) is False:
            liste.remove(i)
    return liste

print my_filter(lambda x: x > 20, l)
