from multiprocessing import Pool


def f(t):
    name, a, b, c = t
    return name, a + b + c


def main():
    data = [('bla', 1, 3, 7), ('spam', 12, 4, 8), ('eggs', 17, 1, 3)]

    p = Pool()
    results = p.map(f, data)
    print(results)


if __name__ == '__main__':
    main()
