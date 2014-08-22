#coding: utf-8
import sys
file_name = sys.argv[1]

my_file = open(file_name, "r")
line_number = 0
letter_number = 0

for line in my_file:
    line_number = line_number + 1
    linex = line.split()
    for word in linex:
        letter_number = letter_number + len(word)

print "line number is %d" % line_number
print "letter number is %d" % letter_number


def read_words(f):
    f.seek(0)
    return f.read().split()


def word_frequency(words):
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency

print word_frequency(read_words(my_file))
