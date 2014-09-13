def reject(f, liste):
    for i in liste:
        if f(i):
            print i
            liste.remove(i)
    return liste

print reject(lambda x: x > 5, [1, 4, 2, 5, 7, 6, 8, 3, 8, 2, 42, 9])


#this code has problems
