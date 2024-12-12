import numpy as np
# read input
with open("input/09", "r") as f:
    data = f.read().strip()

data = list(map(int, list(data)))
print(sum(data))
print(len(data))

fid = np.array(data[0::2])
flen = data[1::2]

# expand data
isfile = True
expanded = []
for id, n in enumerate(data):
    id //= 2
    if isfile:
        for _ in range(n+1):
            expanded.append(id)
        else:
            expanded.append(-1)
    isfile = not isfile
