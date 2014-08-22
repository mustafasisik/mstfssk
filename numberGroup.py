from sys import argv

limit = int(argv[1])
group = int(argv[2])
listem = ["ahmet", 2, "can", "return", 23, 5]


def use_as_list(liste, group_number):
    son_list = []
    while liste:
        son_list.append(liste[:group_number])
        liste = liste[group_number:]
    return son_list


def use_as_range(limit_number, group_number):
    liste1 = range(limit_number)
    return use_as_list(liste1, group_number)


print(use_as_list(listem, group))
print(use_as_range(limit, group))
