import sys
fileName = sys.argv[1]
cikti = open(fileName, "r")
import os
for line in cikti:
    linex = line.split()
    key = linex[0]+".txt"
    value = linex[1]+"\n"
    if not os.path.exists(fileName):
        open(key, "w+").close()
    newfile = open(key, "a")
    newfile.write(value)
    newfile.close()
