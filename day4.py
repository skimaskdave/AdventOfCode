def part2(lines):
    combos_to_check = [""] * 2

    for i in range(len(lines)):
        lines[i] = "Q" + lines[i] + "Q"

    outer_pad = "Q" * (len(lines) + 2)
    lines.insert(0, outer_pad)
    lines.append(outer_pad)

    total = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "A":
                combos_to_check[0] = lines[i-1][j-1]+lines[i][j]+lines[i+1][j+1]
                combos_to_check[1] = lines[i-1][j+1]+lines[i][j]+lines[i+1][j-1]
                if combos_to_check.count("SAM") + combos_to_check.count("MAS") == 2:
                    total += 1

    print(total)


def part1(lines):
    combos_to_check = [""] * 8

    # add padding to outside of grid
    for i in range(len(lines)):
        lines[i] = "QQQ" + lines[i] + "QQQ"

    # add padding to top and bottom
    outer_pad = "QQQ" * (len(lines) + 6)
    for i in range(3):
        lines.insert(0, outer_pad)
        lines.append(outer_pad)

    # look at every direction
    total = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "X":
                combos_to_check[0] = lines[i][j:j + 4]
                combos_to_check[1] = lines[i][j] + lines[i - 1][j + 1] + lines[i - 2][j + 2] + lines[i - 3][j + 3]
                combos_to_check[2] = lines[i][j] + lines[i - 1][j] + lines[i - 2][j] + lines[i - 3][j]
                combos_to_check[3] = lines[i][j] + lines[i - 1][j - 1] + lines[i - 2][j - 2] + lines[i - 3][j - 3]
                combos_to_check[4] = lines[i][j] + lines[i + 1][j] + lines[i + 2][j] + lines[i + 3][j]
                combos_to_check[5] = lines[i][j] + lines[i + 1][j + 1] + lines[i + 2][j + 2] + lines[i + 3][j + 3]
                combos_to_check[6] = lines[i][j] + lines[i][j - 1] + lines[i][j - 2] + lines[i][j - 3]
                combos_to_check[7] = lines[i][j] + lines[i + 1][j - 1] + lines[i + 2][j - 2] + lines[i + 3][j - 3]
                total += combos_to_check.count("XMAS")

    print(total)


data = open("input/day4.txt", "rt").read()
rows = data.split("\n")
part1(rows)
part2(rows)
