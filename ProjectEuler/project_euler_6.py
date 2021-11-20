sumOfSquare = 0
ourSum = 0
for i in range(1, 101):
    sumOfSquare += i*i
    ourSum += i
print(ourSum*ourSum - sumOfSquare)

