stooges = [{"name": 'moe', "age": 40}, {"name": 'larry', "age": 90}, {"name": 'curly', "age": 60}]


def minimum(d, word):
    return min([x[word] for x in d])


print minimum(stooges, "age")
