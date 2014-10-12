def without(liste, l):
    return [x for x in liste if not x in l]


print without([1,2,3,4,5,6,2,34,4,2], [1,2,4])
assert without([1,2,3,4,5,6,2,34,4,2], [1,2,4]) == [3,5,6,34]

