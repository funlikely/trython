import math


# first triangular number with over 500 divisors


def triangle(z):
    return z * (z + 1) / 2


def divisor_counter(a):
    if a < 0:
        return
    if a == 0 or a == 1:
        return 1
    count = 1
    for i in range(2, int(a / 2) + 1):
        if a % i == 0:
            count += 1
    return count + 1


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


# test triangle
for j in range(10):
    print(str(j) + "th triangle number = " + str(triangle(j)))

# test divisor_counter
for p in range(100):
    print(str(p) + " has " + str(divisor_counter(p)) + " divisors!")

# test get_primes
print("The first 1000 primes are " + str(get_primes(1000)))

# test prime_factors
for n in range(50):
    print("The prime factors of " + str(n) + " are " + str(prime_factors(n)) + " and the number of divisors is " +
          str(divisor_counter_fast(n)))

answerFound = False
triangleStep = 12000
max_divisor_count = 2
while not answerFound and triangleStep < 20000:
    current_divisor_count = divisor_counter_fast(triangle(triangleStep))
    if current_divisor_count > 500:
        answerFound = True
        print(str(triangle(triangleStep)) + " has " + str(current_divisor_count) + " divisors!")
    if triangleStep % 250 == 0:
        print("Trying out triangle(" + str(triangleStep) + ") by the way, and it has " + str(current_divisor_count) +
              " divisors.")
    if current_divisor_count > max_divisor_count:
        max_divisor_count = current_divisor_count
        print("New leader in divisors is triangle(" + str(triangleStep) + ") with " + str(
            max_divisor_count) + " divisors")
    triangleStep += 1

if not answerFound:
    print("You must go higher than triangle(" + str(triangleStep) + ")")
