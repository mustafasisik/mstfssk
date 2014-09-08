def f(x):
    return x*x


def each(liste, f):
    for i in liste:
        print f(i)


print f(4)
each([1, 2, 3, 4, 5], f)
assert f(4) == 16
