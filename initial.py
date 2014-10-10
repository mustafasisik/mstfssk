def initial(liste):
    return liste[:-1]


print initial([1,2,3,4,5,6])
assert initial([23,423,423,63423,43323]) == [23,423,423,63423]
