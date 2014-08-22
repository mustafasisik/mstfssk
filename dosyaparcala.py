import sys
file_name = sys.argv[1]

my_file = open(file_name, "r")
line_number, word_number, letter_number = 0, 0, 0
frequency = {}

for line in my_file:
    line_number = line_number + 1
    linex = line.split()
    for w in linex:
        word_number = word_number + 1
        letter_number = letter_number + len(w)
        #frequency[w] = frequency.get("w", 0) + 1

print "line number is: %d" % line_number
print "\nwords number is: %d" % word_number
print "\nletter_number is: %d" % letter_number
#print "\nwords frequency is:\n %r" % frequency
