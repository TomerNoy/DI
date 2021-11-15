# python ---------------------------------------
import numpy as np
import random

table = []

M = 3
N = 3

for i in range(N):
    row = []
    for j in range(M):
        ran = random.randint(1, 100)
        row.append(ran)
    table.append(row)
print(table)

print(table[2])

print([x[2] for x in table])

table[2] = N * [7]
print(table)

table = [x[0:2] + [sum(x[0: 2])] for x in table]
print(table)


# numpy ----------------------------------------

M = 3
N = 3

table = np.random.randint(100, size=(M, N))

table

table[2]

table[:3, 2:3]

table[-1] = 7

table

table[:, -1] = table[:, 0:-1].sum(axis=1)

print(table)
