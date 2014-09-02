my_file = open("She.txt", "r")


def reverse_text(file_name):
    print file_name.readlines()[::-1]


def write_reverse_order(file_name):
    open("reversed_she.txt", "w").writelines(file_name.readlines()[::-1])
    print("New File Created")


write_reverse_order(my_file)
