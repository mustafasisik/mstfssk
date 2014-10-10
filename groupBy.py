def groupBy(f, liste):
    d = {}
    for x in liste:
        if f(x) in d:
            d[f(x)].append(x)
        else:
            d[f(x)] = [x]

    return d


print groupBy(int, [2.4, 1.3, 1.5, 4.6, 4.3, 4.4])
