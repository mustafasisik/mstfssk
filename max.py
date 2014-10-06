stooges = [{"name": 'moe', "age": 40}, {"name": 'larry', "age": 90}, {"name": 'curly', "age": 60} ]


def maximu(d, word):
    return max([x[word] for x in d])


print maximu(stooges, "age")
