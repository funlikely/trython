# found this in python subreddit
# https://old.reddit.com/r/Python/comments/l60ulm/so_guido_posted_this_a_few_hours_ago_on_twitter/
# https://blog.kevmod.com/2014/06/what-does-this-print-1/


x = 999
y = 999


def f():
    x = 1
    y = 1

    class C:
        print(x, y)  # What does this print?
        x = 2


f()



a = "tacos are great"
b = "burritos are great"


def f():
    a = "the world is on fire"
    b = "the house is on fire"

    class C:
        print(a, b)  # What does this print?
        a = "2"
        # b = "0"


f()
