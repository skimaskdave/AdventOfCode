# David Grasmeder AoC 2022 solution to day 6 part 2
f = open("input.txt", "rt")
lines = f.read()
start = False
i = 0
chars = []
while i < len(lines) and not start:
    if len(chars) == 14:
        start = True
    else:
        if lines[i] in chars:
            for j in range(chars.index(lines[i])+1):
                chars.pop(0)
        chars.append(lines[i])
        i += 1

print(i)
