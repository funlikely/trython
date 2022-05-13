# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

collatz_chain = [1] * int(10e8)

print("length of initialized array = " + str(len(collatz_chain)))
collatz_chain[0] = 0

letsa_maximum = 50

def get_collatz_chain_value(i):
    # base case
    if i == 1:
        return collatz_chain[i]
    # the answer has been calculated, we know because the default value is 1
    if collatz_chain[i] != 1:
        return collatz_chain[i]
    # even case
    if i % 2 == 0:
        collatz_chain[i] = 1 + get_collatz_chain_value(int(i / 2))
        return collatz_chain[i]
    # odd case
    collatz_chain[i] = 1 + get_collatz_chain_value(3 * i + 1)
    return collatz_chain[i]


for i in range(2, letsa_maximum):
    if collatz_chain[i] == 1:
        collatz_chain[i] = get_collatz_chain_value(i)
    if i % 100 == 0:
        print("processing i = " + str(i) + ", max(collatz_chain) = " + str(max(collatz_chain)))


print(collatz_chain[:letsa_maximum])
print(max(collatz_chain))


