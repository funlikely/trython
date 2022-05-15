# Number letter counts
#
# Problem 17
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

ones_letter_list = [['', 0], ['one', 3], ['two', 3], ['three', 5], ['four', 4], ['five', 4], ['six', 3], ['seven', 5],
                    ['eight', 5], ['nine', 4]]

teens_letter_list = [['ten', 3], ['eleven', 6], ['twelve', 6], ['thirteen', 8], ['fourteen', 8], ['fifteen', 7],
                     ['sixteen', 7], ['seventeen', 9], ['eighteen', 8], ['nineteen', 8]]

tens_letter_list = [['', 0], ['', 0], ['twenty', 6], ['thirty', 6], ['forty', 5], ['fifty', 5], ['sixty', 5],
                    ['seventy', 7], ['eighty', 6], ['ninety', 6]]


# strategy
# 1-9 : ones
# 10-19 : teens
# 20, 30, ..., 90 : tens
# 21-29, 31-39, ..., 91-99 : ones * 8 + tens * 9
#
# so, 1-99 : ones * 9 + teens + tens * 10 --> subhundreds
#
# 100, 200, ..., 900 : ones + 'hundred' (7) * 9 --> hundreds
# 101-199, 201-299, ..., 901-999 : (hundreds + 'and' (3) * 9) * 99

ones = 0
for i in range(len(ones_letter_list)):
    ones += ones_letter_list[i][1]
print("ones : {0}".format(str(ones)))

teens = 0
for i in range(len(teens_letter_list)):
    teens += teens_letter_list[i][1]
print("teens : {0}".format(str(teens)))

tens = 0
for i in range(len(tens_letter_list)):
    tens += tens_letter_list[i][1]
print("tens : {0}".format(str(tens)))

subhundreds = ones * 9 + teens + tens * 10
print("subhundreds : {0}".format(str(subhundreds)))

hundreds = ones + 7 * 9
hundreds_ands = (hundreds + 3 * 9) * 99

total = hundreds + hundreds_ands + 11

print(total)

num_list = []
for i in range(1, 1001):
    if i == 1000:
        num_list.append('one thousand')
        continue

    hundreds_string = ''
    if 99 < i < 1000:
        hundreds_string = ones_letter_list[int(i/100)][0] + ' hundred'
    if i > 100 and i % 100 != 0:
        hundreds_string += ' and '

    if i % 100 < 10:
        num_list.append(hundreds_string + ones_letter_list[i % 100][0])
        continue
    if i % 100 < 20:
        num_list.append(hundreds_string + teens_letter_list[i % 100 - 10][0])
        continue
    if i % 10 == 0:
        num_list.append(hundreds_string + tens_letter_list[int((i % 100)/10)][0])
        continue

    num_string = tens_letter_list[int((i % 100)/10)][0] + '-' + ones_letter_list[(i % 100) % 10][0]
    num_list.append(hundreds_string + num_string)
    continue

for i in range(1000):
    print(num_list[i])

letter_count = 0
for i in range(1000):
    num_list[i] = num_list[i].replace(' ', '')
    num_list[i] = num_list[i].replace('-', '')
    letter_count += len(num_list[i])

print(letter_count)




