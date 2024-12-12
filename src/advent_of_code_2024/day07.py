# read input
with open("input/07", "r") as f:
    data = f.read().strip().split("\n")

data = [row.split(": ") for row in data]
data = [(int(result), [int(n) for n in eq.split(" ")]) for result, eq in data]


ops = "+*|"

def add_op(acc, remaining, expected):
    if len(remaining) == 0:
        if acc == expected:
            return acc
        else:
            return None
    if acc > expected:
        return None

    for op in ops:
        match op:
            case "*":
                newacc = acc * remaining[0]
            case "+":
                newacc = acc + remaining[0]
            case "|":
                newacc = int(f"{acc}{remaining[0]}")
        # print(acc_, op, remaining[0], " = ", acc, remaining[1:])
        result = add_op(newacc, remaining[1:], expected)
        if result == expected:
            return result


result = 0
for expected, eq in data[:]:
    print(expected, eq)
    r = add_op(eq[0], eq[1:], expected)
    if r == expected:
        result += expected

print(result)
