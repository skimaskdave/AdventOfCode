# David Grasmeder AoC 2022 solution to day 2 part 1

f = open("input.txt", "rt")
moves = []
for line in f:      # get each line in the file
    line = line.strip()
    moves.append(line)

total = 0
for m in moves:
    if m[0] == "A":
        if m[2] == "X":
            total += 3      # draw
            total += 1      # used rock
        elif m[2] == "Y":
            total += 6      # win
            total += 2      # used paper
        elif m[2] == "Z":
            total += 0      # loss
            total += 3      # used scissors
        else:
            print("Something has gone terribly wrong.")
    elif m[0] == "B":
        if m[2] == "X":
            total += 0      # loss
            total += 1      # used rock
        elif m[2] == "Y":
            total += 3      # draw
            total += 2      # used paper
        elif m[2] == "Z":
            total += 6      # win
            total += 3      # used scissors
        else:
            print("Something has gone terribly wrong.")
    elif m[0] == "C":
        if m[2] == "X":
            total += 6      # win
            total += 1      # used rock
        elif m[2] == "Y":
            total += 0      # loss
            total += 2      # used paper
        elif m[2] == "Z":
            total += 3      # draw
            total += 3      # used scissors
        else:
            print("Something has gone terribly wrong.")
    else:
        print("Something has gone very wrong.")

print(total)
