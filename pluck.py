def pluck(liste, word):
    return [x[word] for x in liste]


stooges = [{"name": 'moe', "age": 40}, {"name": 'larry', "age": 50}, {"name": 'curly', "age": 60}]

print pluck(stooges, "name")
