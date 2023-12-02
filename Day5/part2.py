# David Grasmeder AoC 2022 solution to day 5 part 2
import re

f = open("input.txt", "rt")
toggle = False
moves = []
stack_lines = []
for line in f:
    if line == "\n":
        toggle = True
    if not toggle:
        stack_lines.append(line)
    else:
        if line.strip() != "":
            moves.append(line.strip())

stacks = [[], [], [], [], [], [], [], [], []]
for i in range(len(stack_lines) - 1):       # get stacks sorted
    temp = [stack_lines[i][x:x+4] for x in range(0, len(stack_lines[i]), 4)]
    for j in range(len(temp)):
        if temp[j].strip() != "":
            stacks[j].append(temp[j].strip())

regex = "\d"
instructions = []
for instr in moves:     # gets instructions for crates
    temp = []
    dets = instr.split(" ")
    for d in dets:
        if re.search(regex, d):
            temp.append(int(d))
    instructions.append(temp)

for instr in instructions:
    temp = []
    for i in range(instr[0]):
        temp.insert(0, stacks[instr[1]-1].pop(0))
    for t in range(instr[0]):
        stacks[instr[2] - 1].insert(0, temp.pop(0))

for s in stacks:
    print(s)

for s in stacks:
    print(s.pop(0), end="")
