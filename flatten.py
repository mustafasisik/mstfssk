def flatten(liste):
    l = []
    for x in liste:
        if x is list:
            flatten(x)
            print "mustafa"
        else:
            l.append(x)
            print "deneme"
    return l


print flatten([1, [2], [3, [[4]]]])

