employees = [
    ("Smith", "Lucy"),
    ("Jones", "Janet"),
    ("Lee", "Jerry"),
    ("Jackson", "Peter"),
    ("Johnson", "Rick"),
    ("Lewis", "Terry"),
    ("Clarke", "Robin"),
]


def adjust_name(name):
    (last, first) = name
    return f"{last.upper()}, {first}"


employees_adjusted = list(map(lambda per: adjust_name(per), employees))

print("\n".join(employees_adjusted))
