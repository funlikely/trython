# Special Pythagorean triplet
#
# Problem 9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


for a in range(1000):
    for b in range(a, 1000):
        if a > b:
            continue
        if a + b > 999:
            continue
        c = 1000 - a - b
        if a < b < c and (a * a + b * b == c * c) and a + b + c == 1000:
            print("a = " + str(a) + ", b = " + str(b) + ", c = " + str(c) + ", a + b + c = " + str(
                a + b + c) + ", a^2 + b^2 = " + str(a * a + b * b) + ", c^2 = " + str(c * c) + ", a*b*c = " + str(a * b * c))
