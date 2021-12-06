# Advent of Code

# Day 1 Problem 2
# now we need to compare 3-measurement windows

import pandas as pd

numlist = pd.read_csv('input_01.csv', header=None).values

sums = []
change = []

for i in range(len(numlist) - 2):
    sums.append(sum(numlist[i:i+3]))

for j in range(len(sums) - 1):
    diff = sums[j+1] - sums[j]
    change.append(diff)

inc = [1 for x in change if x > 0]

print(sum(inc))

