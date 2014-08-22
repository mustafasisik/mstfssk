from sys import argv
script, word_name, file_one, file_two = argv

file_one = open(file_one, "r")
file_two = open(file_two, "r")

line_number = 0
frequency_one = 0
frequency_two = 0
word_line_one = {}
word_line_two = {}

def find_values(file_name):
