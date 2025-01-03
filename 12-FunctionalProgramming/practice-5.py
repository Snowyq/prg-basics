num_list = list(range(1, 21))
is_divided_by = lambda el, n: el % n == 0

output = list(filter(lambda el: is_divided_by(el, 2) or is_divided_by(el, 3), num_list))

print(output)
