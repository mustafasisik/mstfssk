def difference(list1, list2):
    return [x for x in list1 if not x in list2]


print difference([1,2,34,3,2,4,2],[1,2,1,311])
assert difference([1,2,34,3,2,4,2],[1,2,1,311]) == [34, 3, 4]
