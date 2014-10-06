def invoke(f, liste):
    return [f(x) for x in liste]


#test method
assert invoke(sorted, [[1, 2, 3], [4, 96, 2, 56], [6, 2, 4]]) == [[1, 2, 3], [2, 4, 56, 96], [2, 4, 6]]
