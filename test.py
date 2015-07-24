import re

shakes = open("wssnt10.txt", "r")
love = open("love.txt", "w")

for line in shakes:
    if re.match("(.*)(L|l)ove(.*)", line):
        print >> love, line,
