# Advent of Code

# Day 2 Problem 1

import pandas as pd

mvmt = pd.read_csv('input_02.csv', header=None)

moves = mvmt[0:][0].tolist()

loc = [0, 0] # x dist, depth

for item in moves:
    action, dist = item.split(' ')[0], int(item.split(' ')[1])
    if action == 'forward':
        loc[0] += dist
    elif action == 'down':
        loc[1] += dist
    else:
        loc[1] -= dist
    if loc[1] < 0:
        loc[1] = 0
    
print(loc[0] * loc[1])

