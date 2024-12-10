data = open("inputs/day6.txt", "rt").read()
guard_map = data.split("\n")
for i in range(len(guard_map)):
    guard_map[i] = list(guard_map[i])

positions = []
for x in range(len(guard_map)):
    for y in range(len(guard_map[x])):
        if guard_map[x][y] == "^":
            positions.append((x, y))
            break

leave_map = False
x, y = positions[len(positions)-1]
while not leave_map:
    if guard_map[x][y] == "^":
        if x == 0:
            leave_map = True
        elif guard_map[x-1][y] == "#":
            guard_map[x][y] = ">"
        elif guard_map[x-1][y] == "X":
            guard_map[x][y] = "X"
            guard_map[x - 1][y] = "^"
            x -= 1
        else:
            guard_map[x][y] = "X"
            guard_map[x - 1][y] = "^"
            x -= 1
            positions.append((x, y))
    if guard_map[x][y] == ">":
        if y == len(guard_map[0])-1:
            leave_map = True
        elif guard_map[x][y+1] == "#":
            guard_map[x][y] = "V"
        elif guard_map[x][y+1] == "X":
            guard_map[x][y] = "X"
            guard_map[x][y+1] = ">"
            y += 1
        else:
            guard_map[x][y] = "X"
            guard_map[x][y + 1] = ">"
            y += 1
            positions.append((x, y))
    if guard_map[x][y] == "<":
        if y == 0:
            leave_map = True
        elif guard_map[x][y - 1] == "#":
            guard_map[x][y] = "^"
        elif guard_map[x][y - 1] == "X":
            guard_map[x][y - 1] = "<"
            guard_map[x][y] = "X"
            y -= 1
        else:
            guard_map[x][y] = "X"
            guard_map[x][y - 1] = "<"
            y -= 1
            positions.append((x, y))
    if guard_map[x][y] == "V":
        if x == len(guard_map)-1:
            leave_map = True
        elif guard_map[x + 1][y] == "#":
            guard_map[x][y] = "<"
        elif guard_map[x + 1][y] == "X":
            guard_map[x][y] = "X"
            guard_map[x+1][y] = "V"
            x += 1
        else:
            guard_map[x][y] = "X"
            guard_map[x + 1][y] = "V"
            x += 1
            positions.append((x, y))

print(len(positions))
