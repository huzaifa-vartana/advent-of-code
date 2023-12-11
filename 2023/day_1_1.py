# Project: AdventOfCode2023
# Author: Huzaifa
# Day 1: Day 1: Trebuchet?!

# one, two, three, four, five, six, seven, eight, and nine

valid_words = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:
digit_str = ""

total = 0

with open('/Users/huzaifa/Personal/advent-of-code/2023/input.txt') as f:
    for line in f:
        digits = []
        for idx, starting_char in enumerate(line):
            if starting_char.isdigit():
                digits.append(int(starting_char))
            else:
                curr_digit = ""
                for letter in line[idx:]:
                    curr_digit += letter
                    if curr_digit in valid_words:
                        digits.append(valid_words[curr_digit])


# concat first and last digit and add to total
        total += int(str(digits[0]) + str(digits[-1]))


print(total)
