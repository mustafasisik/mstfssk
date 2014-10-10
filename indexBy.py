stooges = [{"name": 'moe', "age": 40}, {"name": 'larry', "age": 50}, {"name": 'curly', "age": 60}]


def indexBy(liste, key):
    d = {}
    for x in liste:
        d[x[key]] = x

    return d


print indexBy(stooges, "age")
