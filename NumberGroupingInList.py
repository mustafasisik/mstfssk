from sys import argv
limit = int(argv[1])
group = int(argv[2])
base_number = 0
liste = []
while limit > 0:
    liste.append(range(base_number, min(group, limit) + base_number))
    base_number += group
    limit -= group
#liste.append(range(base_number, base_number + limit))
print liste
