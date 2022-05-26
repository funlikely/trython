# Non-abundant sums
#
# Problem 23
#
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


import math


def prime_sieve(n):
    sieve = [True] * n * int(n ** (0.5) + 1)
    sieve[0] = sieve[1] = False
    prime_list = []
    primes_found = 0
    sieve_counter = 2
    while sieve_counter < len(sieve) and primes_found < n:
        if sieve[sieve_counter]:
            primes_found = primes_found + 1
            prime_list.append(sieve_counter)
            sieve_action_counter = sieve_counter * 2
            while sieve_action_counter < len(sieve):
                sieve[sieve_action_counter] = False
                sieve_action_counter += sieve_counter
        sieve_counter += 1
    for sieve_counter in range(sieve_counter, len(sieve)):
        sieve[sieve_counter] = False

    # print(str(primes_found) + ' primes found!')
    return sieve


def get_primes(n):
    primeList = []
    sieve = prime_sieve(n)
    for i in range(2, len(sieve)):
        if sieve[i]:
            primeList.append(i)
    return primeList


prime_list = get_primes(int(5000))


def prime_factors(n):
    prime_list_iter = 0
    prime_factor_list = []
    while prime_list_iter < len(prime_list) and n > 1:
        prime_factor_list.append(0)
        while n % prime_list[prime_list_iter] == 0:
            n /= prime_list[prime_list_iter]
            prime_factor_list[prime_list_iter] += 1
        prime_list_iter += 1
    return [prime_list[:len(prime_factor_list)], prime_factor_list]


def get_divisors(n):
    prime_factor_list = prime_factors(n)
    divisor_list = [1]
    for i in range(len(prime_factor_list[1])):
        new_divisor_list = []
        for j in range(prime_factor_list[1][i] + 1):
            for k in range(len(divisor_list)):
                if j > 0:
                    new_divisor_list.append(int(math.pow(prime_factor_list[0][i], j)) * divisor_list[k])
        divisor_list += new_divisor_list
    divisor_list = list(dict.fromkeys(divisor_list))
    divisor_list.sort()
    return divisor_list[:(len(divisor_list) - 1)]


our_max = 28124
divisor_sum_lookup = [0] * our_max

for i in range(1, our_max):
    if i < len(divisor_sum_lookup) and divisor_sum_lookup[i] != 0:
        divisor_sum = divisor_sum_lookup[i]
    else:
        divisor_sum = sum(get_divisors(i))
        divisor_sum_lookup[i] = divisor_sum
    if i % 2000 == 0:
        print("divisor sum lookup calculation {0} out of {1}".format(str(i), str(our_max)))

# print("Here are a bunch of abundant numbers and their abundant divisor sums")
# print([[i, divisor_sum_lookup[i]] for i in range(1, our_max) if divisor_sum_lookup[i] > i])


abundant_numbers = [i for i in range(1, our_max) if divisor_sum_lookup[i] > i]

sum_possible_list = [False] * 28124
for i in range(len(abundant_numbers)):
    for j in range(len(abundant_numbers)):
        if i <= j and abundant_numbers[i] + abundant_numbers[j] < our_max:
            sum_possible_list[abundant_numbers[i] + abundant_numbers[j]] = True
    if i % 1000 == 0:
        print("{0} out of {1} calculation of non abundant sums".format(str(i), str(our_max)))

non_abundant_sums = [i for i in range(len(sum_possible_list)) if not sum_possible_list[i]]
print("non abundant sums")
print(non_abundant_sums)

print("the sum of all the positive integers which cannot be written as the sum of two abundant numbers is ")
print(sum(non_abundant_sums))

