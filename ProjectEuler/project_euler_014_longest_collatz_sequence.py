# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

collatz_chain = [1] * int(10e8)

print("length of initialized array = " + str(len(collatz_chain)))
collatz_chain[0] = 0

letsa_maximum = 5000


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


def engage_in_a_test_run():
    for i in range(2, letsa_maximum):
        if collatz_chain[i] == 1:
            collatz_chain[i] = get_collatz_chain_value(i)
        if i % 100 == 0:
            print("processing i = " + str(i) + ", max(collatz_chain) = " + str(max(collatz_chain)))
    print(collatz_chain[:letsa_maximum])
    print(max(collatz_chain))


# test run
# engage_in_a_test_run()

def get_remaining(number_tracker):
    count = 0
    for i in range(int(10e6)):
        if not number_tracker[i]:
            count += 1
    return count


def get_remaining_numbers(number_tracker):
    remainders = []
    for i in range(int(1e6)):
        if number_tracker[i] is False:
            remainders.append(i)
    return remainders


def produce_collatz_via_tree(n):
    remaining = 1000000
    max_num_to_track = 2e8
    number_tracker = [False] * int(max_num_to_track)
    collatz_tree = [[1]]
    remaining -= 1
    number_tracker[1] = True
    max_depth = 400
    for i in range(1, max_depth):
        collatz_tree.append([])
        for j in range(len(collatz_tree[i - 1])):
            num = collatz_tree[i - 1][j]
            if 2 * num < max_num_to_track and number_tracker[2 * num] is False:
                collatz_tree[i].append(2 * num)
                number_tracker[2 * num] = True
                if 2 * num < 1000000:
                    remaining -= 1
            if num > 4 and (num - 1) % 3 == 0 and (num - 1) % 6 != 0 and number_tracker[int((num - 1) / 3)] is False:
                collatz_tree[i].append(int((num - 1) / 3))
                number_tracker[int((num - 1) / 3)] = True
                if (num - 1) / 3 < 1000000:
                    remaining -= 1
        collatz_tree[i].sort()
        print("i = {0}, count = {1}, remaining = {2}, elements: {3}".format(str(i), str(len(collatz_tree[i])),
            str(remaining),
            str(collatz_tree[i][:100])))
        if i > 4:
            collatz_tree[i-2] = []
    #print("remaining numbers: " + str(get_remaining_numbers(number_tracker)))
    return collatz_tree




# for i in range(len(tree)):
#     print(tree[i][:100])

def collatz(n):
    chain = str(n)
    count = 1
    while n != 1 and count < 500:
        count += 1
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3 * n + 1
        chain = chain + ", " + str(n)
    return [count, chain]


tree = produce_collatz_via_tree(1)

print(collatz(50226564))

print(collatz(13))