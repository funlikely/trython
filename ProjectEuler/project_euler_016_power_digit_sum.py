# Power digit sum
#
# Problem 16
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

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


n = '0' * 320 + '1'

for i in range(1000):
    n = add_two_string_ints(n, n)
    print('{0} : {1}'.format(str(i + 1).rjust(4, " "), n))

power_digit_sum = 0
for i in range(len(n)):
    power_digit_sum += int(n[i])

print("power digit sum = {0}".format(str(power_digit_sum)))







