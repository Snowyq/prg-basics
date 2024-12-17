temps = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

is_positive = lambda el: el > 0


pos_temps = list(filter(lambda item: is_positive(item[1]), temps.items()))

print(pos_temps)
print("\n".join(map(lambda el: f"{el[0]}", pos_temps)))
