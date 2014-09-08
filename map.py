def square(x):
    return x**2

l = [1, 2, 3, 4, 5, 6]


def my_map(f, liste):
    for i in liste:
        print f(i)


assert square(3) == 9
