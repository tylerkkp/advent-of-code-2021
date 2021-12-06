# Advent of Code

# Day 1 Problem 1

import pandas as pd

numlist = pd.read_csv('input_01.csv', header=None).values

change = []

for i in range(len(numlist) - 1):
    diff = numlist[i+1] - numlist[i]
    change.append(diff)

inc = [1 for x in change if x > 0]

print(sum(inc))

