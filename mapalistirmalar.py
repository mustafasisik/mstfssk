from numberGroup import use_as_list as ual

d = {1:"bir", 2:"iki", 3:"uc", 4:"dort", 5:"bes"}
m = [1,2,3,5,7,9,23,64,4,3,2,1,1,5]

def read(k):
    return d[k]




print map(lambda x: ual(map(lambda y: y**2, x), 1), ual([1,2,3,5,7,9], 3))


#print filter(lambda x: x > 5, m)


def my_filter(f, liste):
    li = []
    for i in liste:
        if f(i):
            li.append(i)
    return li

#print my_filter(lambda x: x > 5, m)


def my_map(f, liste):
    li = []
    for i in liste:
        li.append(f(i))
    return li


#print my_map(lambda x: use_as_list(my_map(lambda y: y**2, x), 1), use_as_list(m, 3))


def dubs(liste):
    l = set(liste)
    return list(set(liste-l))
