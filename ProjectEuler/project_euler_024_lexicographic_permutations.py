# Lexicographic permutations
#
# Problem 24
#
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
#
# 10! permutations
# 3628800 permutations
# 10 sets of 362880
# The 1000000th permutation will be the 274240th permutation starting with 2
# And then the 32320th permutation starting with 7
# And then the 2080th permutation starting with 8
# and then the 640th permutation starting with 3
# ...

import math

# digits = '012'
# digits_dict = dict.fromkeys(digits)
# print(digits_dict)
# permutations = []

# example 1000000 th permutation of 10 items, a = 10, n = 1000000


def generate_permutation_pattern(a, n):
    result = []
    remainder = n
    for i in range(a - 1, 0, -1):
        result.append(int(remainder / math.factorial(i)))
        remainder %= math.factorial(i)
    return result


# generate the nth lexicographical permutation of string or list l
def generate_permutation(l, n):
    result = []
    a = len(l)
    l = sorted(l)
    pattern = generate_permutation_pattern(a, n)
    for i in range(a - 1):
        selected = l[pattern[i]]
        result.append(selected)
        l.remove(selected)
    result += l
    return result


print(generate_permutation('9876543210', 5))
print(generate_permutation('65432', 5))



#print( generate_permutation_pattern(3, 4))
#print( generate_permutation_pattern(5, 1))


for i in range(120):
    print(generate_permutation_pattern(5, i))

for i in range(120):
    print(''.join(generate_permutation('43210', i)))

print(''.join(generate_permutation('9876543210', 1000000)))
