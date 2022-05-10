# https://projecteuler.net/problem=8
# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?


sequenceOfDigits = ""

sequenceOfDigits += "73167176531330624919225119674426574742355349194934"
sequenceOfDigits += "96983520312774506326239578318016984801869478851843"
sequenceOfDigits += "85861560789112949495459501737958331952853208805511"
sequenceOfDigits += "12540698747158523863050715693290963295227443043557"
sequenceOfDigits += "66896648950445244523161731856403098711121722383113"
sequenceOfDigits += "62229893423380308135336276614282806444486645238749"
sequenceOfDigits += "30358907296290491560440772390713810515859307960866"
sequenceOfDigits += "70172427121883998797908792274921901699720888093776"
sequenceOfDigits += "65727333001053367881220235421809751254540594752243"
sequenceOfDigits += "52584907711670556013604839586446706324415722155397"
sequenceOfDigits += "53697817977846174064955149290862569321978468622482"
sequenceOfDigits += "83972241375657056057490261407972968652414535100474"
sequenceOfDigits += "82166370484403199890008895243450658541227588666881"
sequenceOfDigits += "16427171479924442928230863465674813919123162824586"
sequenceOfDigits += "17866458359124566529476545682848912883142607690042"
sequenceOfDigits += "24219022671055626321111109370544217506941658960408"
sequenceOfDigits += "07198403850962455444362981230987879927244284909188"
sequenceOfDigits += "84580156166097919133875499200524063689912560717606"
sequenceOfDigits += "05886116467109405077541002256983155200055935729725"
sequenceOfDigits += "71636269561882670428252483600823257530420752963450"


def getProduct(sequence, start, length):
    product = 1
    for j in range(0, length):
        product *= int(sequence[start+j])
    return product

def getStringDescribingProduct(sequence, start, length):
    result = ''
    for j in range(0, length):
        result += sequence[start+j] + '*'
    return result[:-1]

maxIndex = 1
maxProduct = 0
lenOfProduct = 13 #constant
lenOfSequenceOfDigits = len(sequenceOfDigits)

print('the digits list has ' + str(lenOfSequenceOfDigits)+ ' digits in it.')

productOfDigits = [0] * (len(sequenceOfDigits) - (lenOfProduct-1))
stringOfDigits = [''] * (len(sequenceOfDigits) - (lenOfProduct-1))
currentMax = 0

for i in range(0, len(sequenceOfDigits) - (lenOfProduct-1)):
    productOfDigits[i] = getProduct(sequenceOfDigits, i, lenOfProduct)
    stringOfDigits[i] = getStringDescribingProduct(sequenceOfDigits, i, lenOfProduct)
    if productOfDigits[i] > currentMax:
        print("your current maximum is the " + str(i) + "th product, which is  is " + str(productOfDigits[i]) + " = " + str(stringOfDigits[i]))
        currentMax = productOfDigits[i]

print("Let the people know the answer is " + str(currentMax))



