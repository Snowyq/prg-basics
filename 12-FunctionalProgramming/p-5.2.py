from functools import reduce

numbers = [2, 4, 6, 3, 7, 5]

even_nums = lambda items: list(filter(lambda el: el % 2 == 0, items))


def sum_even(items):
    return reduce(lambda x, y: x + y, items)


print(sum_even(numbers))
