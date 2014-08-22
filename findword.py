from sys import argv
script, wordname, file_name = argv

my_file = open(file_name, "r")
line_number = 0
frequency = 0
word_line = {}

for line in my_file:
    line_number = line_number + 1
    if wordname in line:
        frequency = frequency + 1
        word_line[line_number] = wordname


print "The word we have searched is: %s\n" % wordname
print "frequency is: %d\n" % frequency
print "line number of words: %r" % word_line

