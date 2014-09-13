def some(f, liste):
    for i in liste:
        if f(i):
            return True
    return False


assert some(lambda x: x>5, [1,2,3,4,5,67,8,9]) == True
assert some(lambda x: x>5, [67,8,9]) == True
assert some(lambda x: x>5, [1,2,3,4]) == False
