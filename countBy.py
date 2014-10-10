def countBy(f, liste):
    d = {}
    for x in liste:
        if f(x) in d:
            d[f(x)] += 1
        else:
            d[f(x)] = 1

    return d


print countBy(int, [2.4, 1.3, 1.5, 4.6, 4.3, 4.4])
