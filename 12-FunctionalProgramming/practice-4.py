num_list = list(range(1, 21))

nums_power = lambda items, n: list(map(lambda el: el**n, items))

print(nums_power(num_list, 3))
