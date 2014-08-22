import sys
file_name = sys.argv[1]

my_file = open(file_name, "r")
line_number, word_number, letter_number = 0, 0, 0
frequency = {}


def read_line_number(line, n):
    return n + 1


def read_word_number(liste, n):
    return n + len(liste)


def read_letter_number(liste, n):
    for w in liste:
        n = n + len(w)
    return n


for line in my_file:
    line_number = read_line_number(line, line_number)
    spl = line.split()
    word_number = read_word_number(spl, word_number)
    letter_number = read_letter_number(spl, letter_number)


print line_number, word_number, letter_number
