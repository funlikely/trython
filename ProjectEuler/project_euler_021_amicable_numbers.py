# Amicable numbers
#
# Problem 21
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
# amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

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


def prime_factors(n):
    prime_list = get_primes(int(500))  # that should be enough for now
    prime_list_iter = 0
    prime_factor_list = []
    while prime_list_iter < len(prime_list) and n > 1:
        prime_factor_list.append(0)
        while n % prime_list[prime_list_iter] == 0:
            n /= prime_list[prime_list_iter]
            prime_factor_list[prime_list_iter] += 1
        prime_list_iter += 1
    return [prime_list[:len(prime_factor_list)], prime_factor_list]


def divisor_counter_fast(n):
    prime_factor_list = prime_factors(n)[1]
    for k in range(len(prime_factor_list)):
        prime_factor_list[k] += 1
    return math.prod(prime_factor_list)


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


print(prime_factors(12))


print(get_divisors(7200))

sum_of_amicable_numbers = 0
for i in range(10000):
    sum_of_divisors = sum(get_divisors(i))
    if i % 100 == 0:
        print("sum of divisors of " + str(i) + " = " + str(sum_of_divisors))
    amicable_test = sum(get_divisors(sum_of_divisors))
    if amicable_test == i and i != sum_of_divisors:
        sum_of_amicable_numbers += i
        print("amicable numbers " + str(i) + " and " + str(sum_of_divisors))

print("sum of amicable numbers = " + str(sum_of_amicable_numbers))

