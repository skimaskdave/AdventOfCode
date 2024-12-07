def partial_check(levels):
    last_diff = 0
    unsafe_reports = False

    for i in range(len(levels) - 1):
        diff = int(levels[i]) - int(levels[i + 1])
        if diff == 0:
            unsafe_reports = True
        elif abs(diff) > 3:
            unsafe_reports = True
        else:
            if last_diff > 0 > diff:
                unsafe_reports = True
            elif last_diff < 0 < diff:
                unsafe_reports = True
        last_diff = diff

    return unsafe_reports


def check_surroundings(levels, i):
    fine = False

    if i < len(levels) - 1:
        if not partial_check(levels[:i + 1] + levels[i + 2:]):
            fine = True
    if not fine:
        if not partial_check(levels[:i] + levels[i + 1:]):
            fine = True
    if i > 0 and not fine:
        if not partial_check(levels[:i - 1] + levels[i:]):
            fine = True

    return fine


def part2(ls):
    safe_reports = 0

    for report in ls:
        last_diff = 0
        unsafe_reports = 0
        levels = report.split(" ")

        for i in range(len(levels) - 1):
            diff = int(levels[i]) - int(levels[i + 1])
            if diff == 0:
                if not check_surroundings(levels, i):
                    unsafe_reports += 1
            elif abs(diff) > 3:
                if not check_surroundings(levels, i):
                    unsafe_reports += 1
            else:
                if last_diff > 0 > diff:
                    if not check_surroundings(levels, i):
                        unsafe_reports += 1
                elif last_diff < 0 < diff:
                    if not check_surroundings(levels, i):
                        unsafe_reports += 1
            last_diff = diff

        if unsafe_reports < 1:
            safe_reports += 1

    print(safe_reports)


def part1(ls):
    safe_reports = 0

    for report in ls:
        levels = report.split(" ")
        unsafe_reports = partial_check(levels)

        if not unsafe_reports:
            safe_reports += 1

    print(safe_reports)


data = open("inputs/day2.txt", "rt")
lines = data.read().split("\n")
part1(lines)
part2(lines)
