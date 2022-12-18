import numpy as np


with open('input.txt') as f:
    data = f.readlines()

cal_sums = list()
for group in "".join(data)[:-1].split('\n\n'):
    cal_sums.append(np.array(list(map(int, group.split('\n')))).sum())

cal_sums = np.sort(cal_sums)[::-1]
top3 = cal_sums[:3].sum()

print(f'The maximum number of calories is {top3}')