def contains(x, liste):
    if x in liste:
        return True
    else:
        return False

assert contains(2, [1, 2, 3, 4, 5]) == True
assert contains(1, [3,4,5,6]) == False
