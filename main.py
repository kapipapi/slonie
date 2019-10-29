import sys
from math import inf

lines = sys.stdin.readlines()
n = int(lines[0].replace('\n', ''))
m = [int(i) for i in lines[1].replace('\n', '').split(' ')]
a = [int(i) - 1 for i in lines[2].replace('\n', '').split(' ')]
b = [int(i) - 1 for i in lines[3].replace('\n', '').split(' ')]

t = [False for i in range(n)]
cycles = []
sum = 0

b_index = [None] * n
for idx in range(n):
    b_index[b[idx]] = idx

for i in range(n):
    global_min = min(m)
    if not t[i]:
        x = i
        cycle = []

        while not t[x]:
            t[x] = True
            cycle.append(x)
            x = b_index[a[x]]

        cycle_mass = 0
        cycle_len = len(cycle)
        tmp_min = inf

        for i in cycle:
            cycle_mass += m[a[i]]
            if m[a[i]] < tmp_min:
                tmp_min = m[a[i]]

        sum_m1 = cycle_mass + (cycle_len - 2) * tmp_min
        sum_m2 = cycle_mass + tmp_min + (cycle_len + 1) * global_min
        sum += min(sum_m1, sum_m2)

print(sum)
