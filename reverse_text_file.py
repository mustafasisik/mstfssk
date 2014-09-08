my_file = open("tahir.txt", "r")


def reverse_text(file_name):
    print file_name.readlines()[::-1]


def write_reverse_order(file_name):
    open("hasangorsun.txt", "w").writelines(file_name.readlines()[::-1])
    print("New File Created")


write_reverse_order(my_file)
