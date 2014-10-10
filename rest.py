def rest(liste):
    return liste[1:]


print rest([2,3,1,45,6,3])
assert rest([2,3,1,45,6,3]) == [3,1,45,6,3]
