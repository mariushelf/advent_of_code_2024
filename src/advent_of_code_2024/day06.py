import numpy as np

# read input
with open("inputs/06", "r") as f:
    data = f.readlines()

data = [list(line) for line in data]
data = np.array(data)

obstacles = data == "#"
visited = np.isin(data, (">", "<", "^", "v"))
print(visited.sum())
position = np.argwhere(visited)[0]
print(position)
direction = data[tuple(position)]
print(direction)


def turn_right(direction: str):
    match direction:
        case ">":
            return "v"
        case "<":
            return "^"
        case "^":
            return ">"
        case "v":
            return "<"


def velocity(direction: str):
    match direction:
        case ">":
            return np.array([0, 1])
        case "<":
            return np.array([0, -1])
        case "^":
            return np.array([-1, 0])
        case "v":
            return np.array([1, 0])


while (0 <= position[0] < data.shape[0]) and (0 <= position[1] < data.shape[1]):
    visited[tuple(position)] = True
    next_pos = position + velocity(direction)
    while data[tuple(next_pos)] == "#":
        direction = turn_right(direction)
        next_pos = position + velocity(direction)
    position = next_pos


result = visited.sum()
print(visited)
print(f"Result: {result}")
