import numpy as np


with open('input.txt') as f:
    data = f.readlines()

cal_sums = list()
for group in "".join(data)[:-1].split('\n\n'):
    cal_sums.append(np.array(list(map(int, group.split('\n')))).sum())

answer = np.array(cal_sums).max()

print(f'The maximum number of calories is {answer}')