test_results = [
    {"name": "Peter", "result": 27},
    {"name": "Anna", "result": 63},
    {"name": "Robert", "result": 92},
    {"name": "Paul", "result": 46},
    {"name": "Barbara", "result": 52},
]

print(
    "\n".join(
        list(
            map(
                lambda el: str(el),
                list(
                    filter(
                        lambda item: item["result"] >= 50 and item["result"] <= 70,
                        test_results,
                    )
                ),
            )
        )
    )
)
