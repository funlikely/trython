# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
#
# 1 : 1
# 3 : 1 + (1 * 4) + 2 * 10 = 25
# 5 : 25 + (9 * 4) + 4 * 10 = 101
# 7 : 101 + (25 + 6) + (25 + 6 * 2) + (25 + 6 * 3) + (25 + 6 * 4) = 101 + (25 * 4) + (6 * 10) = 261
# 9 : answer(7) + 7*7*4 + 8*10 = 261 + 196 + 80 = 457+80 = 537
# 11 : answer(9) + 9*9*4 + 10*10 = 537 + 324 + 100 = 981
# n : answer(n-2) + 4(n-2)^2 + 10(n-1)

# looks quadratic, say let's look at differences. Well, it isn't.
# 1, 25, 101, 261, 537, 981
# 24, 76, 160, 276, 444
# 52, 84, 116, 168
# 32, 32, 52

def generate_square_diagonals_sums(limit):
    fake_answer = {1: 1, 3: 25, 5: 101, 7: 261, 1001: 'bad input'};
    if limit % 2 != 1:
        return fake_answer
    real_answer = {1: 1}
    for i in range(3, limit + 2, 2):
        real_answer[i] = real_answer[i - 2] + 4 * (i - 2) * (i - 2) + 10 * (i - 1)
    return real_answer


def main():
    square_diagonals_sums = generate_square_diagonals_sums(1001)
    # print(f"The first couple diagonal sums are {list(square_diagonals_sums.values())[:6]}")
    print(f"The Answer to Project Euler 028 is {square_diagonals_sums[1001]}")


if __name__ == "__main__":
    main()

