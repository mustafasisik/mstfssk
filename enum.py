def enum(liste):
    y = len(liste)
    print [(x, liste[x]) for x in range(y)]
    print zip(range(y), liste)


enum([1, 23, 53])
