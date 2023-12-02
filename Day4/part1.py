# David Grasmeder AoC 2022 solution to day 4 part 1

f = open("input.txt", "rt")
pairs = []
for line in f:
    pairs.append(line.strip())

total = 0
for p in pairs:
    elves = p.split(",")
    elf1 = elves[0].split("-")
    elf2 = elves[1].split("-")
    if int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]):     # if elf2 covers all of elf1
        total += 1
    elif int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):     # if elf1 covers all of elf2
        total += 1

print(total)
