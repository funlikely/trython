def primeSieve(n):
    sieve = [True] * n * int(n ** (0.5) + 1)
    sieve[0] = sieve[1] = False
    primeList = []
    primesFound = 0
    sieveCounter = 2
    while sieveCounter < len(sieve) and primesFound < n:
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


primeOrdinalWeWant = 10001
primes = primeSieve(primeOrdinalWeWant)
primesOrdinal = 1
for i in range(2, len(primes)):
    if primes[i]:
        if primesOrdinal < 10 or primesOrdinal > primeOrdinalWeWant - 100:
            print('#' + str(primesOrdinal) + ' = ' + str(i))
        primesOrdinal += 1


