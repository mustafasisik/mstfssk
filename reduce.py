def add(x, y):
    return x + y

l = [1, 2, 3, 4, 5, 6]


def my_reduce(f, liste):
    print "mustafa"
    while len(liste) > 1:
        liste[1] = f(liste[0], liste[1])
        liste = liste[1:]
        print liste


my_reduce(add, l)
assert add(12, 15) == 27
