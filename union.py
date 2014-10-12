def union(liste1, liste2, liste3):
    for x in liste2:
        if not x in liste1:
            liste1.append(x)
    for y in liste3:
        if not y in liste1:
            liste1.append(y)
    return sorted(liste1)


print union([1,23,4,2], [2,3,1,5,7], [3,2,8,0,765,3,7])

