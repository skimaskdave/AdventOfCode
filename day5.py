data = open("inputs/day5.txt").read()
data_split = data.split("\n")
split_index = data_split.index("")
rules = data_split[:split_index]
updates = data_split[split_index+1:]

rules_dict = {}

for rule in rules:
    new_rule = rule.split("|")
    after_key = int(new_rule[0])
    if after_key in rules_dict:
        rules_dict[after_key]["after"].append(int(new_rule[1]))
    else:
        rules_dict[after_key] = {"before": [], "after": [int(new_rule[1])]}

    before_key = int(new_rule[1])
    if before_key in rules_dict:
        rules_dict[before_key]["before"].append(int(new_rule[0]))
    else:
        rules_dict[before_key] = {"before": [int(new_rule[0])], "after": []}

valid_updates = []
invalid_updates = []

for update in updates:
    valid = True
    i = 0
    keys = list(map(int, update.split(",")))
    while i < len(keys) and valid:
        before = keys[:i]
        after = keys[i + 1:]
        before_rules = rules_dict[keys[i]]["before"]
        after_rules = rules_dict[keys[i]]["after"]

        if len(before) > 0:
            for b in before:
                if b in after_rules:
                    valid = False

        if len(after) > 0:
            for a in after:
                if a in before_rules:
                    valid = False

        i += 1

    if valid:
        valid_updates.append(keys)
    else:
        invalid_updates.append(keys)

total = 0

for v in valid_updates:
    total += v[int((len(v)) / 2)]

print(total)

part2_total = 0
for update in invalid_updates:
    for n in range(len(update)-1, 0, -1):
        swapped = False
        for i in range(n):
            if update[i] in rules_dict[update[i+1]]["after"]:
                update[i], update[i+1] = update[i+1], update[i]
                swapped = True
        if not swapped:
            break
    part2_total += update[int(len(update)/2)]
print(part2_total)


