def every(f, liste):
    for i in liste:
        if not f(i):
            return False
    return True

print every(lambda x: x > 5, [6,7,8,9])
