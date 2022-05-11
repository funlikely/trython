import math

# first triangular number with over 500 divisors

def triangle(n):
    return n * (n + 1) / 2


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
    primeList = []
    primesFound = 0
    sieveCounter = 2
    while sieveCounter < len(sieve) and primesFound < n:
        if sieve[sieveCounter]:
            primesFound = primesFound + 1
            primeList.append(sieveCounter)
            sieveActionCounter = sieveCounter * 2
            while sieveActionCounter < len(sieve):
                sieve[sieveActionCounter] = False
                sieveActionCounter += sieveCounter
        sieveCounter += 1
    for sieveCounter in range(sieveCounter, len(sieve)):
        sieve[sieveCounter] = False

    # print(str(primesFound) + ' primes found!')
    return sieve


def get_primes(n):
    primeList = []
    sieve = prime_sieve(n)
    for i in range(2, len(sieve)):
        if sieve[i]:
            primeList.append(i)
    return primeList


def prime_factors(n):
    primeList = get_primes(int(500)) #that should be enough for now
    primeListIter = 0
    primeFactorList = []
    while primeListIter < len(primeList) and n > 1:
        primeFactorList.append(0)
        while n % primeList[primeListIter] == 0:
            n /= primeList[primeListIter]
            primeFactorList[primeListIter] += 1
        primeListIter += 1
    return [ primeList[:len(primeFactorList)], primeFactorList]

def divisor_counter_fast(n):
    primeFactorList = prime_factors(n)[1]
    for k in range(len(primeFactorList)):
        primeFactorList[k] += 1
    return math.prod(primeFactorList)


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
maxdivisorCount = 2
while not answerFound and triangleStep < 20000:
    currentdivisorCount = divisor_counter_fast(triangle(triangleStep))
    if currentdivisorCount > 500:
        answerFound = True
        print(str(triangle(triangleStep)) + " has " + str(currentdivisorCount) + " divisors!")
    if triangleStep % 250 == 0:
        print("Trying out triangle(" + str(triangleStep) + ") by the way, and it has " + str(currentdivisorCount) +
              " divisors.")
    if currentdivisorCount > maxdivisorCount:
        maxdivisorCount = currentdivisorCount
        print("New leader in divisors is triangle(" + str(triangleStep) + ") with " + str(maxdivisorCount) + " divisors")
    triangleStep += 1

if not answerFound:
    print("You must go higher than triangle(" + str(triangleStep) + ")")
