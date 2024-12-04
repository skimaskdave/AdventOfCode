def set_up(ls):
    l1 = []
    l2 = []

    for line in ls:
        line_split = line.split("   ")
        if len(line_split) == 2:
            l1.append(int(line_split[0]))
            l2.append(int(line_split[1]))

    return l1, l2


def part2(l1, l2):
    similarity_score = 0
    total_occurrences = {}
    for num in l2:
        if total_occurrences.get(num) is None:
            total_occurrences[num] = 1
        else:
            total_occurrences[num] += 1

    for num in l1:
        if total_occurrences.get(num) is not None:
            similarity_score += (num * total_occurrences[num])

    print(similarity_score)


def part1(l1, l2):
    total = 0
    l1.sort()
    l2.sort()

    for i in range(len(l1)):
        total += abs(l1[i] - l2[i])
    print(total)


data = open("inputs/day1.txt", "rt")
lines = data.read().split("\n")
list1, list2 = set_up(lines)
part1(list1, list2)
part2(list1, list2)
