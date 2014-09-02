my_file_object = open("she.txt", "r")

frequency = {}
for i in my_file_object.read():
    frequency[i] = frequency.get(i, 0) + 1
print frequency
