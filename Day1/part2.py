# David Grasmeder AoC 2022 solution to day 1 part 2
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

top_three = []
for x in range(3):
    largest = 0
    for i in elves:
        if i > largest:
            largest = i
    elves.remove(largest)
    top_three.append(largest)

print(top_three[0]+top_three[1]+top_three[2])
