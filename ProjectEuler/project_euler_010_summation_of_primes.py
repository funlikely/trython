# Summation of primes
#
# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

def primeSieveUpTo(n):
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    primeList = []
    primesFound = 0
    sieveCounter = 2
    while sieveCounter < len(sieve):
        if sieve[sieveCounter]:
            primesFound = primesFound + 1
            primeList.append(sieveCounter)
            sieveActionCounter = sieveCounter*2
            while sieveActionCounter < len(sieve):
                sieve[sieveActionCounter] = False
                sieveActionCounter += sieveCounter
        sieveCounter += 1
    for sieveCounter in range(sieveCounter, len(sieve)):
        sieve[sieveCounter] = False

    print(str(primesFound) + ' primes found!')
    return sieve


numPrimes = 2000000
primes = primeSieveUpTo(numPrimes)
primesOrdinal = 1
primesSum = 0
for i in range(2, len(primes)):
    if primes[i]:
        primesSum += i

print("The sum of the primes less than " + str(numPrimes) + " is " + str(primesSum))


