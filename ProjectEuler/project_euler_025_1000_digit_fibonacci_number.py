# 1000-digit Fibonacci number
#
# Problem 25
#
# The Fibonacci sequence is defined by the recurrence relation:
#
#     Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#
# Hence the first 12 terms will be:
#
#     F1 = 1
#     F2 = 1
#     F3 = 2
#     F4 = 3
#     F5 = 5
#     F6 = 8
#     F7 = 13
#     F8 = 21
#     F9 = 34
#     F10 = 55
#     F11 = 89
#     F12 = 144
#
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import math


def add_two_string_ints(a, b):
    carry = 0
    total = []
    max_length = max(len(a), len(b))
    a = a.rjust(max_length, '0')
    b = b.rjust(max_length, '0')
    for i in range(max_length):
        digit_sum = int(a[len(a) - i - 1]) + int(b[len(b) - i - 1]) + carry
        if digit_sum > 9:
            carry = 1
            digit_sum -= 10
        else:
            carry = 0
        total.append(str(digit_sum))
    if carry == 1:
        total.append(str(carry))
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
    return result.lstrip('0')


print(multiply_two_string_ints('123', '12'))
print(multiply_two_string_ints('99', '99'))
print(multiply_two_string_ints('99999999999', '99999999999'))
print(multiply_two_string_ints('999999999999999', '999999999999999'))


fibonacci_list = ["0", "1", "1"] + ["0"] * 12497

for n in range(3, 12500):
    fibonacci_list[n] = add_two_string_ints(fibonacci_list[n-1], fibonacci_list[n-2])
    if n < 6:
        print("fibonacci({0}) = {1}".format(str(n), fibonacci_list[n]))
    if len(fibonacci_list[n]) >= 1000:
        print("1000 digits mark, fibonacci({0}) = ".format(str(n)))
        print(fibonacci_list[n])
        break

# print(fibonacci_list)





