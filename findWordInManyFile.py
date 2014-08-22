from sys import argv
my_word = argv[1].lower()

for file_name in argv[2:]:
    frequency = 0
    line_number = 0
    word_line = {}
    my_file = open(file_name, "r")
    for line in my_file:
        line = line.lower()
        line_number += 1
        linex = line.split()

        freq = linex.count(my_word)
        if freq > 0:
            frequency += freq
            word_line[line_number] = my_word
            print line_number, frequency

    my_file.close()

        #print "word frequency in %s is: %d\n" % (file_name, frequency)
        #print "word foun in %r\n" % word_line
