def uniq(liste):
    l = []
    for x in liste:
        if not x in l:
            l.append(x)
    return sorted(l)

print uniq([1,2,4,2,4,2,5,67])
assert uniq([1,2,4,2,4,2,5,67]) == [1,2,4,5,67]
