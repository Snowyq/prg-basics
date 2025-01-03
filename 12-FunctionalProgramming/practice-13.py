import matplotlib.pyplot as plt

results = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7},
]


country_total = list(
    map(
        lambda item: {
            "country": item["country"],
            "total": sum([item["gold"], item["silver"], item["bronze"]]),
        },
        results,
    )
)

plt.xlabel("Country name")
plt.ylabel("medal count")

plt.bar(
    list(map(lambda el: el["country"], country_total)),
    list(map(lambda el: el["total"], country_total)),
)
plt.show()
