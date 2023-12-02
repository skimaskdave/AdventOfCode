# David Grasmeder AoC 2022 solution to day 1 part 1
import re

regex = "\d+.?\d*"
f = open("input.txt", "rt")
elves = []
total = 0
largest = 0
for line in f:
    line = line.strip()
    food = re.search(regex, line)
    if food:
        total += int(line)
    else:
        elves.append(total)
        total = 0

largest = 0
for i in elves:
    if i > largest:
        largest = i

print(largest)
