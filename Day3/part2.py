# David Grasmeder AoC 2022 solution to day 3 part 2
import re

f = open("input.txt", "rt")
rucksacks = []      # all the groups of 3 elves rucksacks
bag = []        # individual groups
count = 0
for line in f:
    if count == 3:
        rucksacks.append(bag)
        bag = []
        count = 0
    count += 1
    bag.append(line.strip())
rucksacks.append(bag)

badges = []
temp = "a"
for group in rucksacks:
    for i in range(len(group[0])):
        for j in range(len(group[1])):
            for k in range(len(group[2])):
                if group[0][i] == group[1][j] and group[0][i] == group[2][k] and group[0][i] != temp:
                    temp = group[0][i]
    badges.append(temp)

upper = "^[A-Z]$"
lower = "^[a-z]$"
total = 0
for item in badges:
    if re.search(upper, item):
        maths = ord(item) - 64 + 26
        total += maths
    elif re.search(lower, item):
        maths = ord(item) - 96
        total += maths
    else:
        print("We have many problems here")

print(total)
