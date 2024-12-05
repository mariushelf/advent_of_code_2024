# read input
with open("inputs/05", "r") as f:
    data = f.read().strip().split("\n")

rules_raw = []
updates = []

for rule in data:
    if rule == "":
        break  # stop at the empty line
    rules_raw.append(rule)

splitix = data.index("")  # find the index of the empty line
rules_raw = data[:splitix]
updates = data[splitix + 1 :]

rules_raw = [rule.split("|") for rule in rules_raw]
rules = {}
for pre, post in rules_raw:
    if post in rules:
        rules[post].add(pre)
    else:
        rules[post] = {pre}

updates = [update.split(",") for update in updates]
print(rules)
print(updates[:3])

# part 1
valid_updates = []
for update in updates:
    start = set()
    end = set(update)
    prohibited_in_end = set()
    valid = True
    for page in update:
        start.add(page)
        end.remove(page)
        prohibited_in_end |= rules.get(page, set())
        if end & prohibited_in_end:
            valid = False
    if valid:
        valid_updates.append(update)


def sum_of_middles(lists):
    result = 0
    for list_ in lists:
        middle = len(list_) // 2
        result += int(str(list_[middle]))
    return result


result = sum_of_middles(valid_updates)

print(f"Result: {result}")

# part 2
invalid_updates = [update for update in updates if update not in valid_updates]

rules = {}
for pre, post in rules_raw:
    if pre in rules:
        rules[pre].add(post)
    else:
        rules[pre] = {post}


class Page:
    """Object which implements comparison operators according to the rules."""

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return other.value not in rules.get(self.value, set())

    def __str__(self):
        return self.value


corrected_updates = []
for update in invalid_updates:
    update = [Page(page) for page in update]
    corrected_updates.append(sorted(update))

result = sum_of_middles(corrected_updates)
print(f"Result: {result}")
