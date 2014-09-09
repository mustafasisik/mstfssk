d = {1 ="Vol", 5 ="Meh", 7 ="Sow", 5 ="Emr"}


def where(x, dic):
    new_dic = {}
    for i in dic:
        if i == x:
            new_dic.add(new_dic[i])
    return new_dic


print where(5, d)
