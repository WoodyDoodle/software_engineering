def mean(data):
    return sum(data) / float(len(data))


def main(**kwargs):
    for i, j in kwargs.items():
        print(f"{i}: Среднее арифметическое = {mean(j)}")


if __name__ == '__main__':
    main(
        a=[20, 15, 25],
        b=[1, 2, 3, 4, 5, 6]
    )