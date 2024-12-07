import re


def part2(memory):
    order = re.findall("do\(\)|don't\(\)", memory)
    commands = re.split("do\(\)|don't\(\)", memory)
    commands_to_get = [0]
    getting_commands = True

    for i in range(1, len(commands)):
        if order[i-1] == "don't()":
            getting_commands = False
        elif order[i-1] == "do()":
            getting_commands = True
        if getting_commands:
            commands_to_get.append(i)

    useful_memory = ""

    for cmd_index in commands_to_get:
        useful_memory += commands[cmd_index]

    part1(useful_memory)


def part1(memory):
    multiplications = re.findall("mul\(\d\d?\d?,\d\d?\d?\)", memory)
    total = 0

    for mult in multiplications:
        x = re.split(",", mult[4:])
        x[1] = x[1][:len(x[1]) - 1]
        total += (int(x[0]) * int(x[1]))

    print(total)


data = open("inputs/day3.txt", "rt")
input_string = data.read()
part1(input_string)
part2(input_string)
