ratings = [
    (17, 15, 16, 17, 15),
    (16, 18, 19, 17, 19),
    (19, 15, 15, 19, 18),
    (18, 17, 19, 15, 16),
]

fix_ratings = list(map(lambda el: sum(sorted(el)[1:-1]), ratings))

print("\n".join(map(lambda el: str(el), fix_ratings)))
