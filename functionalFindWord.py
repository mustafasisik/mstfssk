from sys import argv
script, wordname, file_name = argv

my_file = open(file_name, "r")
line_number = 0
frequency = 0
word_line = {}


def find_word_in_line(lineNumber, freq, w):
    linex = line.split()
    if w in linex:
        word_line[lineNumber] = w
        freq = freq + linex.count(w)
    return freq


for line in my_file:
    line_number += 1
    frequency = find_word_in_line(line_number, frequency, wordname)


print("The word we have searched is: %s\n" % wordname)
print "frequency is: %d\n" % frequency
print "line number of words: %r" % word_line
