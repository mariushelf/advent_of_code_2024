import numpy as np

# read input
with open("input/08", "r") as f:
    data = f.read().strip().split("\n")

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Location(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Location(self.x - other.x, self.y - other.y)

    def __lt__(self, other):
        """Return true iff we are directly left of other or anywhere above other."""
        return (self.y < other.y) or (self.y == other.y and self.x < other.x)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __array__(self):
        return np.array([self.x, self.y])

    def valid(self, X, Y):
        return 0 <= self.x < X and 0 <= self.y < Y


# read coordinates
locations = {}
for y, row in enumerate(data):
    for x, freq in enumerate(row):
        if freq == ".":
            continue
        if freq in locations:
            locations[freq].append(Location(x, y))
        else:
            locations[freq] = [Location(x, y)]

# sort locations
locations = {freq: sorted(coords) for freq, coords in locations.items()}

sweeties = set()

def calc_sweet_spots(a, b):
    d = b - a
    return {a-d, b+d}

def all_sweet_spots(coords):
    global sweeties
    if len(coords) == 1:
        return
    current, coords = coords[0], coords[1:]
    for coord in coords:
        new_sweeties = calc_sweet_spots(current, coord)
        sweeties |= new_sweeties
    all_sweet_spots(coords)

for freq, coords in locations.items():
    all_sweet_spots(coords)


# clean sweet spots
X = len(data[0])
Y = len(data)

result = {s for s in sweeties if s.valid(X, Y)}
print(len(result))


# part 2
X = len(data[0])
Y = len(data)
def calc_sweet_spots2(a, b):
    d = b - a
    ss = set()
    nss = a
    while nss.valid(X, Y):
        ss.add(nss)
        nss -= d

    nss = b
    while nss.valid(X, Y):
        ss.add(nss)
        nss += d
    return ss

def all_sweet_spots2(coords):
    sweeties = set()
    if not coords: return sweeties
    current, coords = coords[0], coords[1:]
    for coord in coords:
        sweeties |= calc_sweet_spots2(current, coord)
    return sweeties | all_sweet_spots2(coords)

result = set()
for freq, coords in locations.items():
    result |= all_sweet_spots2(coords)
# result = {s for s in sweeties if s.valid(X, Y)}
print(len(result))
