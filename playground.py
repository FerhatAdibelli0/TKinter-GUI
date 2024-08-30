def add(*args):
    total = 0
    for num in args:
        total += num
    return total


summ = add(12, 34, 56, 34, 56, 78)
# print(summ)


def calculate(*args, **kwargs):
    for n in args:
        kwargs["number"] += n

    print(kwargs)


calculate(12, 45, number=34, age=56)
