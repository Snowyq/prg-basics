medals = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7},
]

print(
    "\n".join(
        list(
            map(
                lambda el: f'{el["country"]}, {el["gold"]}, {el["silver"]}, {el["bronze"]}',
                list(
                    filter(
                        lambda item: sum([item["gold"], item["silver"], item["bronze"]])
                        >= 10,
                        medals,
                    )
                ),
            )
        )
    )
)
