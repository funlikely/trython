# You are given the following information, but you may prefer to do some research for yourself.
#
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

calendar_month_day_count = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
calendar_month_day_count_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total_month_calendar = {
  1900: calendar_month_day_count
}

for i in range(1901, 2001):
    if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
        total_month_calendar[i] = calendar_month_day_count_leap_year
    else:
        total_month_calendar[i] = calendar_month_day_count

print(total_month_calendar)


# d is a date of form [YYYY, MM, DD] where the elements are integers
def year(d):
    if len(d) != 3:
        print('date of wrong format')
        return -1
    return d[0]


def date_increment(d):
    if not total_month_calendar.__contains__(d[0]):
        print('cannot increment date ' + str(d))
        return -1
    # can do more validation here if you want
    if d[2] < total_month_calendar[d[0]][d[1] - 1]:
        d[2] += 1
        return d
    if d[1] < 12:
        d[2] = 1
        d[1] += 1
        return d
    d[0] += 1
    d[1] = 1
    d[2] = 1
    return d


def day_of_week(day):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return days[day % 7]


# we will iterate from the initial given date up to the final date of concern, from
# 1/1/1900 to 12/31/2000

date = [1900, 1, 1]

sunday_count = 0
day_of_week = 1     # Sun-Sat is 0-6, so 1 = Monday

while year(date) < 2001:
    date = date_increment(date)
    day_of_week = (day_of_week + 1) % 7
    if day_of_week % 7 == 0 and 2001 > date[0] > 1900 and date[2] == 1:
        sunday_count += 1
    if day_of_week % 7 == 0:
        print('Date = {0}, Day of week = {1}, SundayCount = {2}'.format(str(date), day_of_week, str(sunday_count)))

print()
print('the number of sundays = {0}'.format(str(sunday_count)))

