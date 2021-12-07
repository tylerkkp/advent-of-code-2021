# Advent of Code

# Day 2 Problem 1

import pandas as pd

mvmt = pd.read_csv('input_02.csv', header=None)

moves = mvmt[0:][0].tolist()

loc = [0, 0, 0] # x dist, depth, aim

for item in moves:
    action, dist = item.split(' ')[0], int(item.split(' ')[1])
    if action == 'forward':
        loc[0] += dist
        loc[1] += dist * loc[2]
    elif action == 'down':
        loc[2] += dist
    else:
        loc[2] -= dist
    if loc[1] < 0:
        loc[1] = 0
    
print(loc[0] * loc[1])

