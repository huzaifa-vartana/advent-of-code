# Project: AdventOfCode2023
# Author: Huzaifa
# Day 1: Day 1: Trebuchet?!


total_sum = 0
with open('input.txt') as f:
    for line in f:
        digits = [int(x) for x in line if x.isdigit()]
        total_sum += (digits[0] * 10 + digits[-1])
