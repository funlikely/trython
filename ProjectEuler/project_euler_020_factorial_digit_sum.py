# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

import math


def add_two_string_ints(a, b):
    carry = 0
    total = []
    for i in range(min(len(a), len(b))):
        digit_sum = int(a[len(a) - i - 1]) + int(b[len(b) - i - 1]) + carry
        if digit_sum > 9:
            carry = 1
            digit_sum -= 10
        else:
            carry = 0
        total.append(str(digit_sum))
    total.reverse()
    return ''.join(total)


def multiply_two_string_ints(s, t):
    a = []
    for i in range(len(s)):
        a.append(int(s[len(s) - 1 - i]))
    b = []
    for i in range(len(t)):
        b.append(int(t[len(t) - 1 - i]))
    product_list = [0] * (len(a) + len(b))
    for i in range(len(a)):
        for j in range(len(b)):
            product_list[i + j] += a[i] * b[j]
    temp_product = 0
    for i in range(len(product_list)):
        temp_product += int(product_list[i] * math.pow(10, i))
    width = len(product_list) + 1
    sub_product_list = [''] * width
    for i in range(len(product_list)):
        sub_product_list[i] = str(product_list[i]).rjust(width - i, '0').ljust(width, '0')
    result = sub_product_list[0]
    for i in range(1, len(sub_product_list) - 1):
        result = add_two_string_ints(result, sub_product_list[i])

    #return [result, sub_product_list, product_list]
    return result.lstrip('0')


print(multiply_two_string_ints('123', '12'))
print(multiply_two_string_ints('99', '99'))
print(multiply_two_string_ints('99999999999', '99999999999'))
print(multiply_two_string_ints('999999999999999', '999999999999999'))

factorial = "1"
for i in range(1, 100):
    factorial = multiply_two_string_ints(factorial, str(i))

print(factorial)

factorial_digits_total = 0
for i in range(len(factorial)):
    factorial_digits_total += int(factorial[i])
print("the sum of digits in 100! is " + str(factorial_digits_total))