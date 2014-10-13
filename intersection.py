def intersection(list1,list2,list3):
    return [x for x in list1 if x in list2 and x in list3]


print intersection([1,2,3,4,63,6,3,20,23], [2,2,1,5,23,7], [1,23,25,6,3,2,6])

