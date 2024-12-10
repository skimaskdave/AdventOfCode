data = open("input/test.txt").read()
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

print(invalid_updates)
for update in invalid_updates:
    print(update)
    valid = False
    i = 0
    while not valid and i < len(update):
        value = update[i]
        before = update[:i]
        after = update[i + 1:]
        before_rules = rules_dict[update[i]]["before"]
        after_rules = rules_dict[update[i]]["after"]
        change = False

        # while not change and len(before) > 0:
        #     change = False
        #     for b in before:
        #         if b in after_rules:
        #             print("before: " + str(before))
        #             print("after: " + str(after))
        #             after.insert(0, b)
        #             value = b
        #             before.insert(before.index(b), value)
        #             before.remove(b)
        #             change = True
                    # print("before: " + str(before))
                    # print("after: " + str(after))


