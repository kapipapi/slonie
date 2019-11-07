import sys
from math import inf

# read form standard input
lines = sys.stdin.readlines()
n = int(lines[0].replace('\n', ''))
m = [int(i) for i in lines[1].replace('\n', '').split(' ')]
a = [int(i) - 1 for i in lines[2].replace('\n', '').split(' ')]
b = [int(i) - 1 for i in lines[3].replace('\n', '').split(' ')]

# set variables
t = [False for i in range(n)]
b_index = [None for i in range(n)]
global_min = inf
sum = 0

# create output array and find global minimum mass
for i in range(n):
    b_index[b[i]] = i
    if m[i] < global_min:
        global_min = m[i]

for i in range(n):
    if not t[i]:
        x = i
        cycle_len = 0
        cycle_mass = 0
        cycle_min = inf

        # sum cycle mass
        while not t[x]:
            t[x] = True
            cycle_mass += m[a[x]]

            if m[a[x]] < cycle_min:
                cycle_min = m[a[x]]

            cycle_len += 1
            x = b_index[a[x]]

        # check sum for method 1 and method 2
        sum_m1 = cycle_mass + (cycle_len - 2) * cycle_min
        sum_m2 = cycle_mass + cycle_min + (cycle_len + 1) * global_min
        sum += min(sum_m1, sum_m2)

print(sum)
