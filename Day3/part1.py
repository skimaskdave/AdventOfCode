# David Grasmeder AoC 2022 solution to day 3 part 1
import re

f = open("input.txt", "rt")
rucksacks = []
for line in f:
    rucksacks.append(line.strip())

repeats = []
all_repeats = []
for bag in rucksacks:
    repeats.clear()
    bag_comp = int(len(bag) / 2)     # get the max index of a compartment
    for i in range(bag_comp):
        for j in range(bag_comp):
            if bag[i] == bag[bag_comp + j] and bag[i] not in repeats:
                repeats.append(bag[i])
    if len(repeats) != 0:
        for thing in repeats:
            all_repeats.append(thing)

upper = "^[A-Z]$"
lower = "^[a-z]$"
total = 0
for item in all_repeats:
    if re.search(upper, item):
        maths = ord(item) - 64 + 26
        total += maths
    elif re.search(lower, item):
        maths = ord(item) - 96
        total += maths
    else:
        print("We have many problems here")

print(total)
