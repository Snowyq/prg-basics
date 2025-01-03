import matplotlib.pyplot as plt

measures = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

temps = measures.values()
plt.xlabel("City Name")
plt.ylabel("Temperature")
plt.axhline(y=0, linestyle="dotted")
plt.bar(measures.keys(), measures.values())
plt.show()
