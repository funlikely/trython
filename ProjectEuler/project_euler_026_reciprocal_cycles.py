# Reciprocal cycles
#
# Problem 26
#
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators
# 2 to 10 are given:
#
#     1/2	= 	0.5
#     1/3	= 	0.(3)
#     1/4	= 	0.25
#     1/5	= 	0.2
#     1/6	= 	0.1(6)
#     1/7	= 	0.(142857)
#     1/8	= 	0.125
#     1/9	= 	0.(1)
#     1/10	= 	0.1
#
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit
# recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

import math
import sys

current_max_cycles = 1
current_max_denominator = 1
for i in range(1, 1000, 2):
    nine_pattern = 9
    while nine_pattern % i != 0 and i < sys.maxsize / 9 and i % 2 != 0 and i % 5 != 0:
        nine_pattern = 10 * nine_pattern + 9
    if len(str(nine_pattern)) > current_max_cycles:
        current_max_cycles = len(str(nine_pattern))
        current_max_denominator = i
    if (i - 1) % 50 == 0:
        print("i = {0}, current_max_cycles = {1}, current_max_denominator = {2}".format(str(i), str(current_max_cycles), str(current_max_denominator)))

print("max denominator = {0}, max cycles = {1}".format(str(current_max_denominator), str(current_max_cycles)))
